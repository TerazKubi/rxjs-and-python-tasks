import { from } from 'rxjs';
import { filter, map, mergeMap, reduce } from 'rxjs/operators'

let persons = [
    {id: 1, name: "Jan Kowalski"},
    {id: 2, name: "John Doe"},
    {id: 3, name: "Jarek Kaczka"},
]

let ages = [
    {person: 1,age: 18},
    {person: 2,age: 24},
    {person: 3,age: 666}
]

let locations = [
    {person: 1,country: "Poland"},
    {person: 3,country: "Poland"},
    {person: 1,country: "USA"}
]



const avg_poland_age = from(locations).pipe(
    filter(loc => loc.country === "Poland"),
    mergeMap(loc => {
        const id = loc.person;
        const ageEntry = ages.find(age => age.person === id) 
        return ageEntry ? [ageEntry.age] : [];
    }),

    reduce((acc, value) => {
        return {sum: acc.sum + value, count: acc.count + 1}
    }, {sum: 0, count: 0}),

    map(({sum, count}) => sum / count)

)
                

avg_poland_age.subscribe({
    next: avgAge => console.log(`Average age of people in Poland: ${avgAge}`),
    error: err => console.error(err),
    complete: () => console.log('Calculation complete')
})


// Output:

// Average age of people in Poland: 342
// Calculation complete!
