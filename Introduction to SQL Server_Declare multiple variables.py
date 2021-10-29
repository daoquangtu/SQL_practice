#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Declare @start and @stop and @affected
DECLARE @start DATE
DECLARE @stop DATE
DECLARE @affected INT

#SET @start to '2014-01-24'
SET @start = '2014-01-24'
#SET @stop to '2014-07-02'
Set @stop = '2014-07-02'
#Set @affected to 5000
SET @affected = 5000

#Retrieve all rows where event_date is BETWEEN @start and @stop and affected_customers is greater than or equal to @affected.
SELECT 
  description,
  nerc_region,
  demand_loss_mw,
  affected_customers
FROM 
  grid
WHERE
event_date between @start AND @stop
AND affected_customers >= @affected

