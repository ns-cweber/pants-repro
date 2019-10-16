# README

This reproduces the issue that causes this error message:

```bash
timestamp: 2019-10-16T22:04:01.485289
Exception caught: (pants.build_graph.address_lookup_error.AddressLookupError) (backtrace omitted)
Exception message: Build graph construction failed: ExecutionError 1 Exception encountered:
  Exception: Failed to begin read transaction: Resource temporarily unavailable
```

I see this error message when I have two containers running pants commands
concurrently.

1. In one shell, run `docker-compose run my-service ./pants run package:main`.
2. In another shell, run `docker-compose run my-service ./pants run
   package:main`. This command should fail with the above error.
3. In the second shell, run `docker-compose run my-service bash`. Inside the
   spawned bash shell, run `./pants run package:main`. This should start
   running the program correctly and without error.

This is a minimal example. In reality, I want to run several different pants
services, each in their own container and different pants targets. Note in the
./docker-compose.yml file that we create containers for the pants cache and the
`.pants.d` directory.
