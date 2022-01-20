
const countBy = (array: any) => {
    const counts: any = [ {} ];
    array.map((curr: any) => {
        counts[ curr ] ? counts[ curr ] += 1: (counts[ curr ] = 1);
    });
    return counts;
};

export default countBy;