# mongodb schema

```
const Db_Collection=new mongoose.Schema({
    Key1:{
        type:String,
        required:[true,"Must Provide"],
        trim:true,
        maxLength:[20,"Cannot be more than 20 characters],
        minLenght:3,
        match:[/regex/,'Please Provide a valid email],
        unique:true,
        validate:{
            validator:fn,
            message:""
        }
    },
    Key2:{
        type:Boolean,
        default:false,
    },
    Key3:{
        type:Number,
        required:[true,"Must provide Number"],
        default:0
    },
    Key4:{
        type:Date,
        default:Date.now()
    },
     Key5:{
        type:String,
        enum:{
            value:["option1","option2","option3","option4","option5"],
        message:'{Value} is not supported'
        }
    },
    key6:{
        type:mongoose.Types.ObjectId,
        ref:'User',
        required:true
    },
    key7:{
        type:[string],
        required:true
    }
},{timestamps:true, toJSON:{virtuals:true},toObject:{virtuals:true}})

module.exports = mongoose.model('DBCollection',Db_Collection);
```

```
Db_Collection.virtual('reviews',{
    ref:'Review',
    localField:'_id',
    foreignField:'product',
    justOne:'false'
})
```

```
await Product.remove();

Db_Collection.pre('remove',async function(next){
    return this.model('Review').deleteMany({product:this._id});
})
```

```
Db_Collection.index({product:1,user:1},{unique:true});
```

```
Db_Collection.post('save',fn);
```

```
Db_Collection.post('remove',fn);
```

```
Db_Collection.statics.calculateAverageRating=async fn
```

# create

```
dbCollection.create({"key": "value"})
```

```
dbCollection.create([{},{},{},{}])
```

# find

1. finds all documents

```
dbCollection.find({});
```

2. finds one

```
dbCollection.findOne({_id:""});
```

3. Search query

```
dbCollection.find({
    name:{$regex:search, $options:'i'}
});
```

4. Sort

```
dbCollection.find({}).sort('-key1 key2');
```

5. Select

```
dbCollection.find({}).select('key1 key2');
```

6. Limit

```
dbCollection.find({}).limit(number)
```

7. Skip

```
dbCollection.find({}).limit(number).skip(number)
```

8. Filters

```
dbCollection.find({
    price:{ $gt:30 }
});
```

9. findById

```
dbCollection.findById(id);
```

10. populate

```
dbCollection.find({}).populate({path:'Product',select:'name price'}).populate({path:'User',select:'name age'})
```

# delete

```
dbCollection.findOneAndRemove({_id:""});
```

```
dbCollection.deleteMany();
```

```
dbCollection.findByIdAndDelete();
```

# update

```
dbCollection.findOneAndUpdate({_id:""},newDataObject,{new:true,runValidator:true,overwrite:true});
```

```
dbCollection.findByIdAndUpdate({_id:""},newDataObject,{new:true,runValidator:true,overwrite:true});
```

```
dbCollection.save();
```

# aggregation

```
dbCollection.aggregate([
    {$match:{createdBy:mongoose.Types.ObjectId(req.user.userId)}},
    {$group:{_id:'$status',count:{$sum:1}}}
])
```

```
dbCollection.aggregate([
    {$match:{createdBy:mongoose.Types.ObjectId(req.user.userId)}},
    {$group:{
        _id:{
            year:{$year:'$createdAt'},
            month:{$month:'$createdAt'}
        },
        count:{$sum:1}
            }
    },
    {
        $sort:{
            'id.year':-1,'_id.month':-1
            }
    },
    {$limit:6}
])
```

