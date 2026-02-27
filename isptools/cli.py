import typer
import requests
import ipaddress
import sys
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

app = typer.Typer(help="CLI utilities for ISP Network Engineers")
console = Console()

def print_header():
    console.clear()
    console.print("[bold cyan]======================================[/bold cyan]")
    console.print("    [bold yellow] ISP Tools (Built by Xeesan)[/bold yellow]")
    console.print("[bold cyan]======================================[/bold cyan]\n")

def run_subnet(ip_range: str = None):
    print_header()
    if not ip_range:
        ip_range = Prompt.ask("[cyan]Enter IP range in CIDR (e.g., 192.168.1.0/24)[/cyan]")
    
    try:
        network = ipaddress.IPv4Network(ip_range, strict=False)
        
        table = Table(title=f"Subnet Details: {ip_range}", title_style="bold cyan")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Network Address", str(network.network_address))
        table.add_row("Broadcast Address", str(network.broadcast_address))
        table.add_row("Netmask", str(network.netmask))
        table.add_row("Total IPs", str(network.num_addresses))
        
        if network.num_addresses > 2:
            usable = network.num_addresses - 2
            first_host = list(network.hosts())[0]
            last_host = list(network.hosts())[-1]
            table.add_row("Usable IPs", str(usable))
            table.add_row("Usable Range", f"{first_host} - {last_host}")
        else:
            table.add_row("Usable IPs", "0 (Point-to-Point if /31)")
            
        console.print(table)
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] Invalid CIDR notation ({e})")
    print("\n")

def run_mac(address: str = None):
    print_header()
    if not address:
        address = Prompt.ask("[cyan]Enter MAC address (e.g., 00:1A:2B:3C:4D:5E)[/cyan]")
        
    with console.status(f"[cyan]Looking up MAC address: {address}...[/cyan]"):
        try:
            response = requests.get(f"https://api.macvendors.com/{address}", timeout=10)
            
            if response.status_code == 200:
                company = response.text
                console.print(f"\n[bold green]Vendor Found:[/bold green] [cyan]{company}[/cyan]")
            else:
                console.print(f"\n[bold yellow]No vendor found for MAC:[/bold yellow] {address}")
                
        except Exception as e:
            console.print(f"\n[bold red]Error:[/bold red] Failed to look up MAC address ({e})")
    print("\n")

def run_myip():
    print_header()
    with console.status("[cyan]Fetching public IP info...[/cyan]"):
        try:
            response = requests.get("https://ipinfo.io/json", timeout=5)
            data = response.json()
            
            table = Table(title="Public IP Info", title_style="bold cyan")
            table.add_column("Property", style="cyan")
            table.add_column("Value", style="green")

            table.add_row("IP Address", data.get("ip", "N/A"))
            table.add_row("ISP / Org", data.get("org", "N/A"))
            table.add_row("Location", f"{data.get('city', '')}, {data.get('region', '')}, {data.get('country', '')}")
            
            console.print("\n")
            console.print(table)
            
        except Exception as e:
            console.print(f"\n[bold red]Error:[/bold red] Failed to fetch IP info ({e})")
    print("\n")

def interactive_menu():
    while True:
        print_header()
        console.print("Please select a tool by entering its number:\n")
        console.print("[bold cyan]1.[/bold cyan] Subnet Calculator")
        console.print("[bold cyan]2.[/bold cyan] MAC Vendor Lookup")
        console.print("[bold cyan]3.[/bold cyan] Public IP Checker")
        console.print("[bold red]4.[/bold red] Exit\n")
        
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4"])
        
        if choice == "1":
            run_subnet()
            Prompt.ask("[dim]Press Enter to return to menu[/dim]")
        elif choice == "2":
            run_mac()
            Prompt.ask("[dim]Press Enter to return to menu[/dim]")
        elif choice == "3":
            run_myip()
            Prompt.ask("[dim]Press Enter to return to menu[/dim]")
        elif choice == "4":
            console.print("[green]Goodbye![/green]")
            sys.exit(0)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """ISP Tools Command Line Interface"""
    if ctx.invoked_subcommand is None:
        interactive_menu()

# We still expose them as subcommands so power users can bypass the menu if they want
@app.command(name="subnet", help="Calculate subnet details from a CIDR block")
def subnet_cmd(ip_range: str = typer.Argument(..., help="IP range in CIDR")):
    run_subnet(ip_range)

@app.command(name="mac", help="Look up a MAC address vendor")
def mac_cmd(address: str = typer.Argument(..., help="MAC address")):
    run_mac(address)

@app.command(name="myip", help="Check public IP and ISP details")
def myip_cmd():
    run_myip()

if __name__ == "__main__":
    app()
