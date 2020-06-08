
export const countBy = (array) => {
    console.log(array);
    let counts = {};
    array.map((curr) => {
        counts[curr] ? counts[curr]++ : (counts[curr] = 1);
    });
    return counts;
}
