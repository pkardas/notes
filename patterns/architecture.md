[go back](https://github.com/pkardas/learning)

# Architecture Patterns

[TOC]

## Command and Query Responsibility Segregation (CQRS)

Based on: https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs, https://martinfowler.com/bliki/CQRS.html, https://bulldogjob.pl/articles/122-cqrs-i-event-sourcing-czyli-latwa-droga-do-skalowalnosci-naszych-systemow_

This pattern separates read and update operations for a data store. Traditionally the same data model is used to query and update a database. This might work well but for simple CRUD applications. For more complex applications, where there are more advanced operations on read and write sides CQRS might be a better idea.

Commands update data, queries read data. Commands should be *task based*, rather than *data centric* (book hotel room instead of set `reservation_status` to `reserved`). Queries *never* modify the database.

Usually whenever command updates data it is also publishing an event and this needs to be done within single transaction.

![patterns-architecture-cqrs-martin-fowler](../_images/patterns-architecture-cqrs-martin-fowler.png)

CQRS:

- you are able to scale Command and Query independently
- separate models for updating and querying might lead to eventual consistency
- suited for complex domains

## ReportingDatabase

Based on: https://martinfowler.com/bliki/ReportingDatabase.html



## Event Sourcing

Based on: https://docs.microsoft.com/en-us/azure/architecture/patterns/event-sourcing