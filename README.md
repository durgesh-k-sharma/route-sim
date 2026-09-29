# Distance Vector Routing Simulator

This repository contains a Python network simulator and a distance vector router implementation. Routers learn host routes from neighbors, choose lower-cost paths, and forward packets using their routing tables.

## Features

- Route learning with Bellman–Ford updates and route expiration
- Periodic and incremental triggered route advertisements
- Split horizon and poison reverse options
- Poisoning for expired routes and failed links
- A visualizer for inspecting network topologies and packet flow

## Requirements

- Python 3

Change to the `simulator/` directory before you run these commands:

```bash
cd simulator
```

## Run a simulation

Start a basic topology with the distance vector router:

```bash
python3 simulator.py --start --default-switch-type=dv_router topos.simple
```

The simulator's visualizer is available at `http://127.0.0.1:4444` while the process is running. To try other included topologies, replace `topos.simple` with a topology such as `topos.linear`, `topos.square`, or `topos.candy`. Some topologies accept parameters; for example:

```bash
python3 simulator.py --start --default-switch-type=dv_router topos.linear --n=3
```

## Run the tests

Run all stages of the router unit tests:

```bash
python3 dv_unit_tests.py 10
```

To run through a particular stage, replace `10` with its stage number (`1`–`10`).

## Router configuration

The `DVRouter` class is implemented in `dv_router.py`. Its class attributes configure optional routing behavior:

- `SPLIT_HORIZON` and `POISON_REVERSE` control how routes are advertised back toward their source.
- `POISON_EXPIRED` controls whether expired routes are retained as unreachable routes for propagation.
- `POISON_ON_LINK_DOWN` controls whether routes through a failed link are poisoned or removed.
- `SEND_ON_LINK_UP` controls whether the router immediately advertises its routes to a newly connected neighbor.

Split horizon and poison reverse are mutually exclusive. These options are disabled by default.
