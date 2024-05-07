# Write your MySQL query statement below
select id,
if (p_id is null,
    'Root', 
    if ((select count(*) from Tree as mi where mi.p_id=mn.id) >= 1, 
        'Inner',
        'Leaf')) as type
from Tree as mn;