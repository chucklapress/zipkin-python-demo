import os
from datetime import datetime
import sys
from random import randint
from time import sleep

from opencensus.trace.tracer import Tracer
from opencensus.trace import time_event as time_event_module
from opencensus.ext.zipkin.trace_exporter import ZipkinExporter
from opencensus.trace.samplers import AlwaysOnSampler

# create exporter
ze = ZipkinExporter(service_name="simulated_calls",
                                host_name='localhost',
                                port=9411,
                                endpoint='/api/v2/spans')
# set the tracer to use the exporter
# Get the global singleton Tracer object
tracer = Tracer(exporter=ze, sampler=AlwaysOnSampler())

def main():
    # createthe range of sample connections
    with tracer.span(name="main") as span:
        for i in range(0,25):
            signalCall()

def signalCall():
    # Start another span. Because this is within the scope of the "main" span,
    # this will automatically be a child span set random interval for signal.
    with tracer.span(name="signalCall") as span:
        print("now connecting")
        try:
            sleep(randint(1,15))
        except:
            # set status for error
            span.status = Status(5, "Error occurred")

        # annote span with meta data
        span.add_annotation("patching you through")

if __name__ == "__main__":
    main()
