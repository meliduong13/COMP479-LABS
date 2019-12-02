# To run spimi's algorithm:
in 
```__main.py__```
uncomment 
```# spimi(files, disk_files, './DISK/', './DISK_FINAL/')``` 
this will create your final dictionary in the directory '/FINAL_DICT'

# TO make search queries:
run 
```search_final_dict```
to run your query, replace the values in quotation marks after
```query = ```
choose your type of query "or" / "and" and replace the values after
```query_type= ```

# lossy compression techniques results
|                   | distinct terms | non positional postings | number of positional postings |
| ---:              | :---:          | :---:                   |  :---:                        |
| unfiltered        | 147,047        | 2,226,432               | 3,516,607                     |
| no number         | 91,144         | 2,041,816               | 3,459,632                     | 
| case folding      | 73,371         | 1,912,362               | 3,457,905                     |
| 30 stop words     | 73,345         | 1,884,278               | 3,400,090                     | 
| 150 stop words    | 73,232         | 1,562,716               | 2,550,593                     | 
| porter stemming   | 62,060         | 1,501,694               | 2,550,593                     | 


# Query results:

```json
{
    "carter": [854, 965, 1993, 2534, 3380, 5465, 5525, 7061, 10252, 11114, 11118, 11330, 12136, 12677, 13540, 15158, 15473, 16887, 17023, 17325, 17363, 18005, 18438, 18962, 19432, 20614, 21308],
    "jimmy": [12136, 13540, 17023, 18005, 19432, 20614]
}
```

Results for the "and" query "jimmy carter"
```json
[12136, 13540, 17023, 18005, 19432, 20614]
```

*****************************************************

```json
{
    "green": [263, 275, 345, 707, 1249, 1753, 1842, 2162, 2163, 2347, 2404, 2606, 2627, 3397, 3714, 3878, 3885, 4634, 4719, 5107, 5124, 5334, 6698, 7308, 7415, 8193, 9265, 9328, 10230, 10682, 10733, 10752, 10799, 12300, 12655, 12701, 12814, 12878, 13190, 13629, 14427, 14982, 16115, 17415, 17419, 17433, 17583, 18464, 19091, 19430, 19551, 19867, 19960, 20186, 20555, 21118, 21577],
    "party": [28, 60, 219, 222, 226, 234, 308, 319, 337, 338, 428, 704, 871, 967, 1129, 1477, 1594, 1685, 1880, 1900, 1906, 1916, 1957, 2074, 2132, 2228, 2364, 2406, 2467, 2556, 2786, 2823, 2965, 2967, 2972, 3188, 3205, 3313, 3451, 3488, 3502, 3549, 3567, 3597, 3670, 4026, 4070, 4096, 4166, 4247, 4548, 4670, 4674, 4705, 4721, 4736, 4738, 4887, 5030, 5070, 5117, 5161, 5190, 5208, 5221, 5262, 5289, 5325, 5338, 5622, 5774, 6052, 6143, 6156, 6188, 6190, 6345, 6360, 6395, 6396, 6400, 6430, 6899, 6927, 6945, 6989, 7022, 7043, 7477, 7525, 7536, 7549, 7630, 7651, 7777, 7779, 7849, 7927, 7941, 8073, 8091, 8133, 8139, 8307, 8342, 8405, 8450, 8493, 8496, 8627, 8691, 8727, 8884, 8904, 9108, 9126, 9140, 9153, 9183, 9247, 9275, 9292, 9402, 9466, 9479, 9689, 9739, 9761, 9774, 9797, 9847, 9848, 9907, 9921, 9929, 10123, 10210, 10230, 10268, 10271, 10290, 10355, 10379, 10486, 10621, 10646, 10666, 10863, 11172, 11175, 11176, 11243, 11245, 11397, 11442, 11742, 11768, 11779, 11837, 12069, 12322, 12431, 12438, 12440, 12612, 12737, 12750, 12773, 12792, 12876, 12879, 12916, 13082, 13084, 13257, 13260, 13277, 13318, 13323, 13347, 13396, 13414, 13417, 13419, 13420, 13446, 13458, 13527, 13534, 13548, 13564, 13576, 13606, 13627, 13637, 13671, 13692, 13725, 13733, 13752, 13790, 13993, 13995, 14030, 14342, 14357, 14412, 14419, 14631, 14635, 14654, 14710, 14739, 14757, 14780, 14809, 14819, 14825, 14826, 14874, 14905, 14950, 14951, 14976, 15033, 15228, 15342, 15369, 15372, 15373, 15375, 15408, 15450, 15452, 15453, 15456, 15470, 15549, 15795, 15962, 16137, 16181, 16198, 16211, 16226, 16292, 16409, 16727, 16732, 16770, 16774, 16777, 16780, 16787, 16844, 16876, 16902, 17012, 17040, 17043, 17047, 17055, 17070, 17072, 17075, 17170, 17172, 17188, 17222, 17249, 17259, 17272, 17305, 17402, 17432, 17461, 17573, 17681, 17803, 17874, 17893, 17934, 17966, 17970, 18138, 18222, 18375, 18403, 18417, 18449, 18469, 18507, 18597, 18682, 18731, 18915, 19024, 19027, 19034, 19039, 19134, 19157, 19191, 19353, 19405, 19432, 19495, 19508, 19525, 19566, 19588, 19662, 19683, 19751, 19898, 20056, 20061, 20075, 20231, 20379, 20764, 20860, 20911, 20986, 21123, 21276, 21508, 21536, 21547, 21572, 21575, 21577]
}
```

Results for the "and" query "Green Party"
```json
[10230, 21577]
```

*******************************************************

```json
{
    "innovations": [247, 3192, 5230, 5386, 7051, 8483, 16128],
    "telecommunication": [3552, 6535, 12143, 12188, 12459, 17460, 19016, 19035, 21550, 21555]
}
```

Results for the "and" query "Innovations in telecommunication"
```json
[]
```

********************************************************

```json
{
    "ecologist": [],
    "environmentalist": [5774]
}
```

Results for the "or" query "environmentalist ecologist"
```json
[5774]
```
## PROJECT 2

Document length average
```
118.20340161275374
```


Query results for "george bush" with k1=10 b=1

```
document containing keyword(s): ['george', 'bush']
document score:  48.715887114205586
document id:     7525

document containing keyword(s): ['george', 'bush']
document score:  43.195763659278555
document id:     4008

document containing keyword(s): ['george', 'bush']
document score:  42.86499812294893
document id:    20719

document containing keyword(s): ['george', 'bush']
document score:  41.55012087991369
document id:     8500

document containing keyword(s): ['george', 'bush']
document score:  34.01755717991032
document id:    20891

document containing keyword(s): ['george', 'bush']
document score:  33.41461006556978
document id:    16780

document containing keyword(s): ['george', 'bush']
document score:  31.584939993071444
document id:      854

document containing keyword(s): ['george', 'bush']
document score:  31.05501588044188
document id:     3560

document containing keyword(s): ['george', 'bush']
document score:  30.64556426889562
document id:     2796

document containing keyword(s): ['george', 'bush']
document score:  29.951570347840224
document id:      965

document containing keyword(s): ['george', 'bush']
document score:  29.192541825111775
document id:     5405

document containing keyword(s): ['george', 'bush']
document score:  24.627889830639752
document id:     8593

document containing keyword(s): ['george', 'bush']
document score:  23.755349927540948
document id:    20860
```

Results for the query "Democrats' welfare and healthcare reform policies"
No result containing all keywords "Democrats' welfare and healthcare reform policies"

Listed below are the results containing some of the keywords
```
document containing keyword(s): ['reform', 'policies']
document score:  38.63959606222923
document id:    12806

document containing keyword(s): ['reform', 'policies']
document score:  36.76159489483275
document id:    11204

document containing keyword(s): ['reform', 'policies']
document score:  35.90981587833643
document id:    10230

document containing keyword(s): ['reform', 'policies']
document score:  34.0202264370401
document id:    17940

document containing keyword(s): ['reform', 'policies']
document score:  33.648770482869345
document id:     6606

document containing keyword(s): ['reform', 'policies']
document score:  32.972202051067725
document id:    15382

document containing keyword(s): ['reform', 'policies']
document score:  32.4848909329922
document id:    12750

document containing keyword(s): ['reform', 'policies']
document score:  31.889279997916457
document id:    12552

document containing keyword(s): ['reform', 'policies']
document score:  31.74012128675134
document id:     2417

document containing keyword(s): ['reform', 'policies']
document score:  31.69753145589599
document id:     7219

document containing keyword(s): ['welfare', 'reform']
document score:  30.383491413424643
document id:     8072

document containing keyword(s): ['reform', 'policies']
document score:  30.14290717379781
document id:     7375

document containing keyword(s): ['reform', 'policies']
document score:  29.960187525738906
document id:     9055

document containing keyword(s): ['healthcare']
document score:  29.27905092969154
document id:    17697

document containing keyword(s): ['healthcare']
document score:  29.050075913695526
document id:    20686

document containing keyword(s): ['reform', 'policies']
document score:  28.765833129417782
document id:    12879

document containing keyword(s): ['reform', 'policies']
document score:  28.533261310143036
document id:    16226

document containing keyword(s): ['reform', 'policies']
document score:  28.405601587066055
document id:    10355

document containing keyword(s): ['reform', 'policies']
document score:  28.1792486624107
document id:     7493

document containing keyword(s): ['reform', 'policies']
document score:  28.0791620447865
document id:      672

document containing keyword(s): ['welfare']
document score:  27.96835237191924
document id:     2594

document containing keyword(s): ['healthcare']
document score:  27.322855820755898
document id:    17560

document containing keyword(s): ['healthcare']
document score:  27.20612289486309
document id:    19173

document containing keyword(s): ['welfare', 'policies']
document score:  26.696763394044588
document id:     1895

document containing keyword(s): ['healthcare']
document score:  26.58943982554737
document id:    15630

document containing keyword(s): ['reform', 'policies']
document score:  26.563036433686875
document id:     2078

document containing keyword(s): ['healthcare']
document score:  26.541942873849262
document id:     1595

document containing keyword(s): ['reform', 'policies']
document score:  26.420380412348823
document id:    16544

document containing keyword(s): ['welfare']
document score:  25.87338918709064
document id:      225

document containing keyword(s): ['reform', 'policies']
document score:  25.7407801353494
document id:     8310

document containing keyword(s): ['reform', 'policies']
document score:  25.685417418412545
document id:     6940

document containing keyword(s): ['reform', 'policies']
document score:  25.595617264850116
document id:     2132

document containing keyword(s): ['healthcare']
document score:  25.407310292584565
document id:    17740

document containing keyword(s): ['reform', 'policies']
document score:  25.332021292253422
document id:    12438

document containing keyword(s): ['reform', 'policies']
document score:  24.946652362228612
document id:    12598

document containing keyword(s): ['reform', 'policies']
document score:  24.92461145572384
document id:      862

document containing keyword(s): ['welfare']
document score:  24.210996510444218
document id:     3847

document containing keyword(s): ['reform', 'policies']
document score:  24.210050942245402
document id:    20462

document containing keyword(s): ['healthcare']
document score:  24.089190976052798
document id:    19829

document containing keyword(s): ['healthcare']
document score:  24.011334927882793
document id:    20423

document containing keyword(s): ['healthcare']
document score:  23.933980518512975
document id:     5093

document containing keyword(s): ['reform', 'policies']
document score:  23.857825167798026
document id:    20829

document containing keyword(s): ['reform', 'policies']
document score:  23.742683114230843
document id:     6600

document containing keyword(s): ['reform', 'policies']
document score:  23.62864711419281
document id:    14874

document containing keyword(s): ['healthcare']
document score:  23.480122125940014
document id:      535

document containing keyword(s): ['reform', 'policies']
document score:  23.293018327907685
document id:    17070

document containing keyword(s): ['healthcare']
document score:  23.186993242413603
document id:    18722

document containing keyword(s): ['reform', 'policies']
document score:  23.18325091536444
document id:    17402

document containing keyword(s): ['healthcare']
document score:  23.04315636918115
document id:     6323

document containing keyword(s): ['healthcare']
document score:  22.86585047607257
document id:     2916

document containing keyword(s): ['healthcare']
document score:  22.76077063283654
document id:     6276

document containing keyword(s): ['reform', 'policies']
document score:  22.545774576938484
document id:     2052

document containing keyword(s): ["democrats'"]
document score:  22.200497607164607
document id:    19525

document containing keyword(s): ['reform', 'policies']
document score:  22.139916261299724
document id:     8635

document containing keyword(s): ['welfare', 'policies']
document score:  20.919748522689808
document id:     5868

document containing keyword(s): ['welfare']
document score:  20.703968692001027
document id:     8242

document containing keyword(s): ['reform']
document score:  20.68592954733062
document id:    16171

document containing keyword(s): ['reform']
document score:  20.642714301275035
document id:    18731

document containing keyword(s): ['reform']
document score:  20.49162259471486
document id:     2068

document containing keyword(s): ['reform']
document score:  20.4094611527265
document id:    16292

document containing keyword(s): ['reform', 'policies']
document score:  20.35011721536729
document id:     4006

document containing keyword(s): ['healthcare']
document score:  20.276016481715793
document id:     1760

document containing keyword(s): ['reform']
document score:  20.22028958607051
document id:    19134

document containing keyword(s): ['healthcare']
document score:  20.0570570424706
document id:     1188

document containing keyword(s): ['healthcare']
document score:  20.0570570424706
document id:     6329

document containing keyword(s): ['healthcare']
document score:  20.0570570424706
document id:    15791

document containing keyword(s): ['reform']
document score:  20.008342532981185
document id:     6581

document containing keyword(s): ['welfare']
document score:  20.004521773099256
document id:     9248

document containing keyword(s): ['welfare']
document score:  20.004521773099256
document id:    10125

document containing keyword(s): ['reform']
document score:  19.956048207633955
document id:    19877

document containing keyword(s): ['reform']
document score:  19.852275359401677
document id:     4508

document containing keyword(s): ['healthcare']
document score:  19.737343527136694
document id:     3619

document containing keyword(s): ['reform']
document score:  19.698624022737164
document id:    20335

document containing keyword(s): ['welfare', 'policies']
document score:  19.68409865699123
document id:     7892

document containing keyword(s): ['reform']
document score:  19.603793924998353
document id:     4130

document containing keyword(s): ['welfare']
document score:  19.17178419998573
document id:    18941

document containing keyword(s): ['reform']
document score:  19.03563559437199
document id:    11592

document containing keyword(s): ['healthcare']
document score:  19.029561779746643
document id:    10251

document containing keyword(s): ['policies']
document score:  18.889190295492085
document id:    17438

document containing keyword(s): ['policies']
document score:  18.85169787755492
document id:    20061

document containing keyword(s): ['reform']
document score:  18.6588398876878
document id:     9704

document containing keyword(s): ['reform']
document score:  18.652002813761044
document id:    18161

document containing keyword(s): ['healthcare']
document score:  18.64744859039982
document id:     7433

document containing keyword(s): ['welfare']
document score:  18.570527729742796
document id:    11463

document containing keyword(s): ['reform']
document score:  18.550044684837943
document id:     7019

document containing keyword(s): ['reform']
document score:  18.523043832650718
document id:    19157

document containing keyword(s): ['policies']
document score:  18.425034653552302
document id:    20023

document containing keyword(s): ['reform']
document score:  18.415821905453576
document id:    19591

document containing keyword(s): ['reform']
document score:  18.336216557062336
document id:     4268

document containing keyword(s): ['policies']
document score:  18.306655371639028
document id:    16935

document containing keyword(s): ['reform']
document score:  18.250750439891622
document id:     5235

document containing keyword(s): ['reform']
document score:  18.185547485802694
document id:     3366

document containing keyword(s): ['reform']
document score:  18.185547485802694
document id:     3502

document containing keyword(s): ['reform']
document score:  18.131566522871662
document id:    18683

document containing keyword(s): ['policies']
document score:  18.0973621466165
document id:     3124

document containing keyword(s): ['reform']
document score:  18.056529333152753
document id:     8592

document containing keyword(s): ['reform']
document score:  17.96096072403162
document id:     8137

document containing keyword(s): ['policies']
document score:  17.96047185539974
document id:     2242

document containing keyword(s): ['policies']
document score:  17.96047185539974
document id:    21542

document containing keyword(s): ['reform', 'policies']
document score:  17.876104277245727
document id:     6052

document containing keyword(s): ['healthcare']
document score:  17.84137608623513
document id:    20449

document containing keyword(s): ['reform']
document score:  17.772826637951027
document id:    15543

document containing keyword(s): ['reform']
document score:  17.772826637951027
document id:    16778

document containing keyword(s): ['reform']
document score:  17.772826637951027
document id:    18009

document containing keyword(s): ['reform']
document score:  17.772826637951027
document id:    18568

document containing keyword(s): ['reform']
document score:  17.772826637951027
document id:    18642

document containing keyword(s): ['reform']
document score:  17.772826637951027
document id:    19019

document containing keyword(s): ['reform']
document score:  17.58859295954538
document id:     2891

document containing keyword(s): ['policies']
document score:  17.58796775110043
document id:    17953

document containing keyword(s): ['reform', 'policies']
document score:  17.53406854773022
document id:    16168

document containing keyword(s): ['reform']
document score:  17.52802759825153
document id:     3537

document containing keyword(s): ['healthcare']
document score:  17.42296399826477
document id:    19453

document containing keyword(s): ['reform']
document score:  17.40813963802009
document id:     9307

document containing keyword(s): ['reform']
document score:  17.40813963802009
document id:    13592

document containing keyword(s): ['reform']
document score:  17.37842346303487
document id:     8307

document containing keyword(s): ['reform', 'policies']
document score:  17.371135645500573
document id:     8667

document containing keyword(s): ['reform']
document score:  17.36854060358815
document id:    19660

document containing keyword(s): ['reform']
document score:  17.289880552650473
document id:     7549

document containing keyword(s): ['healthcare']
document score:  17.261043100475092
document id:     5659

document containing keyword(s): ['reform']
document score:  17.17321736972416
document id:    13241

document containing keyword(s): ['reform']
document score:  17.17321736972416
document id:    16103

document containing keyword(s): ['reform']
document score:  17.17321736972416
document id:    21455

document containing keyword(s): ['policies']
document score:  17.11879770968532
document id:    18163

document containing keyword(s): ['reform']
document score:  17.058118000781516
document id:       32

document containing keyword(s): ['reform']
document score:  16.98223841523288
document id:     2979

document containing keyword(s): ['reform']
document score:  16.98223841523288
document id:    20091

document containing keyword(s): ['reform']
document score:  16.944551211896403
document id:    10049

document containing keyword(s): ['reform']
document score:  16.944551211896403
document id:    19220

document containing keyword(s): ['reform']
document score:  16.9445512118964
document id:      951

document containing keyword(s): ['policies']
document score:  16.875466027388118
document id:    15456

document containing keyword(s): ['reform']
document score:  16.83248659541844
document id:    10212

document containing keyword(s): ['reform', 'policies']
document score:  16.782704198253068
document id:    16092

document containing keyword(s): ['policies']
document score:  16.75637597143092
document id:    20311

document containing keyword(s): ['policies']
document score:  16.75637597143092
document id:    20795

document containing keyword(s): ['policies']
document score:  16.69745904053688
document id:    17598

document containing keyword(s): ['policies']
document score:  16.65841072304677
document id:    21561

document containing keyword(s): ['reform']
document score:  16.64897032803234
document id:    18507

document containing keyword(s): ['policies']
document score:  16.58085944267475
document id:      570

document containing keyword(s): ['policies']
document score:  16.58085944267475
document id:     1611

document containing keyword(s): ['reform']
document score:  16.576679396771368
document id:     4727

document containing keyword(s): ['policies']
document score:  16.46587699942281
document id:     7105

document containing keyword(s): ['policies']
document score:  16.46587699942281
document id:     7877

document containing keyword(s): ['policies']
document score:  16.46587699942281
document id:    17915

document containing keyword(s): ['reform']
document score:  16.44407703629615
document id:    16777

document containing keyword(s): ['policies']
document score:  16.408981733603532
document id:     3411

document containing keyword(s): ['reform']
document score:  16.372296806784963
document id:     8139

document containing keyword(s): ['policies']
document score:  16.352478299278474
document id:     7401

document containing keyword(s): ['policies']
document score:  16.35247829927847
document id:    11820

document containing keyword(s): ['policies']
document score:  16.35247829927847
document id:    13657

document containing keyword(s): ['policies']
document score:  16.35247829927847
document id:    16540

document containing keyword(s): ['policies']
document score:  16.35247829927847
document id:    18265

document containing keyword(s): ['reform']
document score:  16.346009171708907
document id:    15140

document containing keyword(s): ['reform', 'policies']
document score:  16.333031693338
document id:    17185

document containing keyword(s): ['reform']
document score:  16.241697401808064
document id:     7651

document containing keyword(s): ['policies']
document score:  16.240630844849257
document id:    11163

document containing keyword(s): ['policies']
document score:  16.240630844849257
document id:    21273

document containing keyword(s): ['reform']
document score:  16.190039176746826
document id:       61

document containing keyword(s): ['reform']
document score:  16.190039176746826
document id:     7216

document containing keyword(s): ['reform']
document score:  16.13870851738508
document id:     2883

document containing keyword(s): ['policies']
document score:  16.13030302180361
document id:     8608

document containing keyword(s): ['policies']
document score:  16.13030302180361
document id:     8982

document containing keyword(s): ['policies']
document score:  16.13030302180361
document id:    17450

document containing keyword(s): ['policies']
document score:  16.13030302180361
document id:    18835

document containing keyword(s): ['reform']
document score:  16.06231993080478
document id:     7551

document containing keyword(s): ['policies']
document score:  16.021464069078682
document id:     3246

document containing keyword(s): ['policies']
document score:  16.021464069078682
document id:    18271

document containing keyword(s): ['welfare']
document score:  15.99132161550542
document id:     9096

document containing keyword(s): ['reform']
document score:  15.986651070553876
document id:      335

document containing keyword(s): ['policies']
document score:  15.914084050286212
document id:    17307

document containing keyword(s): ['policies']
document score:  15.914084050286208
document id:     1971

document containing keyword(s): ['reform']
document score:  15.837432221636073
document id:     2965

document containing keyword(s): ['policies']
document score:  15.808133826260558
document id:     6108

document containing keyword(s): ['policies']
document score:  15.808133826260558
document id:     6415

document containing keyword(s): ['policies']
document score:  15.808133826260558
document id:     9462

document containing keyword(s): ['policies']
document score:  15.808133826260558
document id:    14809

document containing keyword(s): ['reform']
document score:  15.788309709135744
document id:     2848

document containing keyword(s): ['reform']
document score:  15.7151946515702
document id:     3670

document containing keyword(s): ['reform']
document score:  15.690973219566747
document id:    17217

document containing keyword(s): ['reform']
document score:  15.64275365850031
document id:     9226

document containing keyword(s): ['reform']
document score:  15.59482955427233
document id:     5345

document containing keyword(s): ['reform']
document score:  15.594829554272328
document id:    17934

document containing keyword(s): ['reform']
document score:  15.499856920325012
document id:     5973

document containing keyword(s): ['reform']
document score:  15.499856920325012
document id:     8151

document containing keyword(s): ['reform']
document score:  15.499856920325012
document id:    21158

document containing keyword(s): ['policies']
document score:  15.298862326345136
document id:     4882

document containing keyword(s): ['reform']
document score:  15.267410300004531
document id:    18469

document containing keyword(s): ['policies']
document score:  15.233428072909044
document id:    17423

document containing keyword(s): ['healthcare']
document score:  15.211234430293016
document id:     3899

document containing keyword(s): ['reform']
document score:  15.161304554853523
document id:     5891

document containing keyword(s): ['policies']
document score:  15.104224523735349
document id:    10633

document containing keyword(s): ['reform']
document score:  15.086413234692833
document id:     8662

document containing keyword(s): ['policies']
document score:  15.008751073924786
document id:     3364

document containing keyword(s): ['policies']
document score:  15.008751073924786
document id:    18625

document containing keyword(s): ['policies']
document score:  15.008751073924786
document id:    21525

document containing keyword(s): ['reform']
document score:  14.866113680294713
document id:    16375

document containing keyword(s): ['policies']
document score:  14.821379883015819
document id:      942

document containing keyword(s): ['policies']
document score:  14.821379883015817
document id:      209

document containing keyword(s): ['reform']
document score:  14.77978487644376
document id:     1105

document containing keyword(s): ['reform']
document score:  14.751230986396202
document id:       54

document containing keyword(s): ["democrats'"]
document score:  14.721456978136635
document id:     9688

document containing keyword(s): ['reform']
document score:  14.694452921419641
document id:     4491

document containing keyword(s): ['healthcare']
document score:  14.670558005724233
document id:     8289

document containing keyword(s): ['policies']
document score:  14.638629339739289
document id:    13722

document containing keyword(s): ['healthcare']
document score:  14.612846118658014
document id:    19133

document containing keyword(s): ['reform']
document score:  14.610100648241389
document id:     7099

document containing keyword(s): ['policies']
document score:  14.593643711920087
document id:     1088

document containing keyword(s): ['policies']
document score:  14.593643711920087
document id:    16006

document containing keyword(s): ['policies']
document score:  14.548933725584913
document id:    15694

document containing keyword(s): ['policies']
document score:  14.460330605413894
document id:    15364

document containing keyword(s): ['policies']
document score:  14.460330605413894
document id:    15552

document containing keyword(s): ['policies']
document score:  14.37280014015562
document id:     8885

document containing keyword(s): ['policies']
document score:  14.37280014015562
document id:    13908

document containing keyword(s): ['policies']
document score:  14.37280014015562
document id:    18159

document containing keyword(s): ['policies']
document score:  14.329431084359937
document id:    15408

document containing keyword(s): ['policies']
document score:  14.286322968204328
document id:    19398

document containing keyword(s): ['reform']
document score:  14.22892748524306
document id:    14749

document containing keyword(s): ['policies']
document score:  14.200880191141145
document id:    15718

document containing keyword(s): ['policies']
document score:  14.200880191141145
document id:    17363

document containing keyword(s): ['policies']
document score:  14.11645335996543
document id:     6426

document containing keyword(s): ['policies']
document score:  14.11645335996543
document id:    15738

document containing keyword(s): ['reform']
document score:  14.045703381813407
document id:    12612

document containing keyword(s): ['policies']
document score:  13.95057590715067
document id:    14270

document containing keyword(s): ['policies']
document score:  13.923307928960986
document id:    10780

document containing keyword(s): ['policies']
document score:  13.788551513015621
document id:     7062

document containing keyword(s): ['reform']
document score:  13.779547147509643
document id:    16196

document containing keyword(s): ['reform']
document score:  13.742346029637298
document id:     1563

document containing keyword(s): ['reform']
document score:  13.742346029637297
document id:    19039

document containing keyword(s): ['policies']
document score:  13.735376502634496
document id:    16827

document containing keyword(s): ['policies']
document score:  13.708942501964879
document id:     5944

document containing keyword(s): ['policies']
document score:  13.708942501964879
document id:    15957

document containing keyword(s): ['reform']
document score:  13.631938190967006
document id:     9180

document containing keyword(s): ['policies']
document score:  13.630247468601299
document id:    12455

document containing keyword(s): ['policies']
document score:  13.630247468601299
document id:    17750

document containing keyword(s): ['policies']
document score:  13.630247468601299
document id:    20925

document containing keyword(s): ['reform']
document score:  13.559313304716458
document id:    12640

document containing keyword(s): ['policies']
document score:  13.55245076292587
document id:    11732

document containing keyword(s): ['reform']
document score:  13.523290275407412
document id:     8743

document containing keyword(s): ['policies']
document score:  13.450092835234015
document id:     2802

document containing keyword(s): ['reform']
document score:  13.381092079573458
document id:    13046

document containing keyword(s): ['reform']
document score:  13.381092079573458
document id:    19017

document containing keyword(s): ['policies']
document score:  13.28701889513732
document id:    15873

document containing keyword(s): ['policies']
document score:  13.249946443455155
document id:     8240

document containing keyword(s): ['reform']
document score:  13.207495091046194
document id:       55

document containing keyword(s): ['reform']
document score:  13.105482240230774
document id:    12039

document containing keyword(s): ['reform']
document score:  13.105482240230774
document id:    18878

document containing keyword(s): ['policies']
document score:  13.10370253936144
document id:    15763

document containing keyword(s): ['policies']
document score:  13.10370253936144
document id:    17420

document containing keyword(s): ['policies']
document score:  13.031784548679733
document id:     8141

document containing keyword(s): ['reform']
document score:  12.971891465223752
document id:     6099

document containing keyword(s): ['reform']
document score:  12.971891465223752
document id:    18985

document containing keyword(s): ['policies']
document score:  12.960651674322815
document id:     7343

document containing keyword(s): ['policies']
document score:  12.94298962559493
document id:    16957

document containing keyword(s): ['reform']
document score:  12.938918239141062
document id:    10664

document containing keyword(s): ['reform']
document score:  12.906112217202988
document id:     7155

document containing keyword(s): ['policies']
document score:  12.890291129615994
document id:    17452

document containing keyword(s): ['reform']
document score:  12.873472130811143
document id:    17242

document containing keyword(s): ['reform']
document score:  12.840996724168116
document id:    13637

document containing keyword(s): ['policies']
document score:  12.820690404049579
document id:     2190

document containing keyword(s): ['reform']
document score:  12.77653498997981
document id:     2415

document containing keyword(s): ['reform']
document score:  12.77653498997981
document id:     9673

document containing keyword(s): ['policies']
document score:  12.751837255863204
document id:     5318

document containing keyword(s): ['policies']
document score:  12.751837255863204
document id:    15224

document containing keyword(s): ['reform']
document score:  12.712717218218401
document id:     9774

document containing keyword(s): ['reform']
document score:  12.712717218218401
document id:    17106

document containing keyword(s): ['policies']
document score:  12.683719704867839
document id:     2278

document containing keyword(s): ['policies']
document score:  12.683719704867839
document id:    12673

document containing keyword(s): ['reform']
document score:  12.681046810253052
document id:    19495

document containing keyword(s): ['healthcare']
document score:  12.647572926323537
document id:     3266

document containing keyword(s): ['welfare']
document score:  12.629378424033646
document id:    10486

document containing keyword(s): ['policies']
document score:  12.616326025496589
document id:     6722

document containing keyword(s): ['reform']
document score:  12.586975345264506
document id:     4059

document containing keyword(s): ['reform']
document score:  12.586975345264506
document id:     7633

document containing keyword(s): ['reform']
document score:  12.525032605894168
document id:     3198

document containing keyword(s): ['policies']
document score:  12.48366461230922
document id:     1999

document containing keyword(s): ['policies']
document score:  12.48366461230922
document id:    17126

document containing keyword(s): ['reform']
document score:  12.463696543385053
document id:    18598

document containing keyword(s): ['policies']
document score:  12.418374640964501
document id:    12519

document containing keyword(s): ['policies']
document score:  12.418374640964501
document id:    12744

document containing keyword(s): ['policies']
document score:  12.418374640964501
document id:    16770

document containing keyword(s): ['reform']
document score:  12.402958288339427
document id:     9445

document containing keyword(s): ['reform']
document score:  12.402958288339427
document id:    10350

document containing keyword(s): ['healthcare']
document score:  12.373727848021765
document id:    19929

document containing keyword(s): ['policies']
document score:  12.353764053759678
document id:    12623

document containing keyword(s): ['policies']
document score:  12.353764053759678
document id:    15549

document containing keyword(s): ['policies']
document score:  12.353764053759678
document id:    17277

document containing keyword(s): ['reform']
document score:  12.342809143411005
document id:       18

document containing keyword(s): ['reform']
document score:  12.303032777997782
document id:     4625

document containing keyword(s): ['policies']
document score:  12.289822301437319
document id:    11327

document containing keyword(s): ['reform']
document score:  12.283240579153171
document id:    18776

document containing keyword(s): ['policies']
document score:  12.22653905202265
document id:     1318

document containing keyword(s): ['policies']
document score:  12.22653905202265
document id:    12828

document containing keyword(s): ['reform']
document score:  12.224244229986892
document id:      238

document containing keyword(s): ['reform']
document score:  12.224244229986892
document id:     6896

document containing keyword(s): ['policies']
document score:  12.19514119520364
document id:     6657

document containing keyword(s): ['reform']
document score:  12.165811890284239
document id:     8835

document containing keyword(s): ['reform']
document score:  12.165811890284239
document id:    19740

document containing keyword(s): ['policies']
document score:  12.16390418525799
document id:     3752

document containing keyword(s): ['policies']
document score:  12.16390418525799
document id:    21508

document containing keyword(s): ['reform']
document score:  12.10793551056372
document id:     5432

document containing keyword(s): ['reform']
document score:  12.10793551056372
document id:    11998

document containing keyword(s): ['policies']
document score:  12.101907787207434
document id:      740

document containing keyword(s): ['policies']
document score:  12.101907787207434
document id:     6190

document containing keyword(s): ['policies']
document score:  12.101907787207434
document id:    12844

document containing keyword(s): ['policies']
document score:  12.101907787207434
document id:    17803

document containing keyword(s): ['reform']
document score:  12.050607193793692
document id:    19600

document containing keyword(s): ['policies']
document score:  12.040540145025622
document id:     8427

document containing keyword(s): ['policies']
document score:  12.040540145025622
document id:    10774

document containing keyword(s): ['policies']
document score:  12.040540145025622
document id:    10800

document containing keyword(s): ['policies']
document score:  12.040540145025622
document id:    17207

document containing keyword(s): ['reform']
document score:  11.99381919180028
document id:    18609

document containing keyword(s): ['policies']
document score:  11.979791741884942
document id:    17410

document containing keyword(s): ['policies']
document score:  11.979791741884942
document id:    18868

document containing keyword(s): ['policies']
document score:  11.979791741884942
document id:    19000

document containing keyword(s): ['policies']
document score:  11.91965325205547
document id:    15442

document containing keyword(s): ['policies']
document score:  11.91965325205547
document id:    15678

document containing keyword(s): ['policies']
document score:  11.860115536132383
document id:     5227

document containing keyword(s): ['reform']
document score:  11.826621752978438
document id:      860

document containing keyword(s): ['reform']
document score:  11.826621752978438
document id:    12718

document containing keyword(s): ['policies']
document score:  11.801169636405705
document id:     6954

document containing keyword(s): ['policies']
document score:  11.801169636405705
document id:     8210

document containing keyword(s): ['policies']
document score:  11.801169636405705
document id:    10344

document containing keyword(s): ['policies']
document score:  11.801169636405705
document id:    20727

document containing keyword(s): ['reform']
document score:  11.771920385355363
document id:     2387

document containing keyword(s): ['policies']
document score:  11.74280677236741
document id:     5516

document containing keyword(s): ['policies']
document score:  11.74280677236741
document id:     5717

document containing keyword(s): ['policies']
document score:  11.74280677236741
document id:    11198

document containing keyword(s): ['policies']
document score:  11.74280677236741
document id:    20678

document containing keyword(s): ['policies']
document score:  11.685018336351236
document id:    10689

document containing keyword(s): ['policies']
document score:  11.685018336351236
document id:    10771

document containing keyword(s): ['policies']
document score:  11.685018336351236
document id:    17382

document containing keyword(s): ['reform']
document score:  11.664021788923334
document id:      428

document containing keyword(s): ['reform']
document score:  11.664021788923334
document id:     2980

document containing keyword(s): ['reform']
document score:  11.664021788923334
document id:    18885

document containing keyword(s): ['reform']
document score:  11.664021788923334
document id:    19321

document containing keyword(s): ['policies']
document score:  11.627795889300574
document id:     2352

document containing keyword(s): ['policies']
document score:  11.627795889300574
document id:    13869

document containing keyword(s): ['policies']
document score:  11.627795889300574
document id:    18041

document containing keyword(s): ['policies']
document score:  11.627795889300574
document id:    20907

document containing keyword(s): ['policies']
document score:  11.571131156660108
document id:     9782

document containing keyword(s): ['policies']
document score:  11.571131156660108
document id:    13752

document containing keyword(s): ['policies']
document score:  11.515016024387023
document id:     5271

document containing keyword(s): ['policies']
document score:  11.459442535077674
document id:     1175

document containing keyword(s): ['policies']
document score:  11.459442535077674
document id:    17312

document containing keyword(s): ['policies']
document score:  11.404402884205918
document id:     8980

document containing keyword(s): ['policies']
document score:  11.404402884205918
document id:    10936

document containing keyword(s): ['reform']
document score:  11.402734960303226
document id:    18726

document containing keyword(s): ['reform']
document score:  11.35187607556606
document id:    19211

document containing keyword(s): ['policies']
document score:  11.349889416469308
document id:     3065

document containing keyword(s): ['policies']
document score:  11.349889416469308
document id:     9694

document containing keyword(s): ['policies']
document score:  11.349889416469308
document id:    17747

document containing keyword(s): ['policies']
document score:  11.349889416469308
document id:    19845

document containing keyword(s): ['reform']
document score:  11.301468861490822
document id:     7595

document containing keyword(s): ['reform']
document score:  11.301468861490822
document id:    12440

document containing keyword(s): ['policies']
document score:  11.295894622239581
document id:     3885

document containing keyword(s): ['policies']
document score:  11.295894622239581
document id:     4736

document containing keyword(s): ['policies']
document score:  11.295894622239581
document id:     6746

document containing keyword(s): ['reform']
document score:  11.27643275485544
document id:    17271

document containing keyword(s): ['reform']
document score:  11.25150732784051
document id:     5453

document containing keyword(s): ['reform']
document score:  11.25150732784051
document id:    19604

document containing keyword(s): ['policies']
document score:  11.189431723564157
document id:     4603

document containing keyword(s): ['policies']
document score:  11.189431723564157
document id:    15470

document containing keyword(s): ['policies']
document score:  11.189431723564157
document id:    16749

document containing keyword(s): ['policies']
document score:  11.189431723564157
document id:    17397

document containing keyword(s): ['policies']
document score:  11.163128825635106
document id:    12456

document containing keyword(s): ['reform']
document score:  11.152897865857698
document id:     4587

document containing keyword(s): ['reform']
document score:  11.152897865857698
document id:     8390

document containing keyword(s): ['policies']
document score:  11.13694929767919
document id:     9639

document containing keyword(s): ['policies']
document score:  11.13694929767919
document id:    13034

document containing keyword(s): ['policies']
document score:  11.13694929767919
document id:    17087

document containing keyword(s): ['policies']
document score:  11.13694929767919
document id:    20500

document containing keyword(s): ['policies']
document score:  11.033447687442381
document id:    17196

document containing keyword(s): ['policies']
document score:  11.033447687442381
document id:    18472

document containing keyword(s): ['policies']
document score:  11.033447687442381
document id:    19976

document containing keyword(s): ['reform']
document score:  11.008182462173398
document id:     5169

document containing keyword(s): ['policies']
document score:  10.982414967304129
document id:     5206

document containing keyword(s): ['policies']
document score:  10.982414967304129
document id:     6392

document containing keyword(s): ['policies']
document score:  10.982414967304129
document id:    11314

document containing keyword(s): ['policies']
document score:  10.982414967304129
document id:    16701

document containing keyword(s): ['reform']
document score:  10.960774963464434
document id:     9549

document containing keyword(s): ['policies']
document score:  10.931852154356637
document id:    19285

document containing keyword(s): ['policies']
document score:  10.915101187127945
document id:    17202

document containing keyword(s): ['reform']
document score:  10.913774041146562
document id:    12431

document containing keyword(s): ['policies']
document score:  10.881752788015149
document id:    14950

document containing keyword(s): ['reform']
document score:  10.86717448722893
document id:    19834

document containing keyword(s): ['policies']
document score:  10.832110525586945
document id:       28

document containing keyword(s): ['policies']
document score:  10.832110525586945
document id:     8747

document containing keyword(s): ['policies']
document score:  10.832110525586945
document id:    16051

document containing keyword(s): ['policies']
document score:  10.832110525586945
document id:    18516

document containing keyword(s): ['policies']
document score:  10.782919139594478
document id:     5759

document containing keyword(s): ['policies']
document score:  10.782919139594478
document id:     7405

document containing keyword(s): ['policies']
document score:  10.782919139594478
document id:     9470

document containing keyword(s): ['policies']
document score:  10.782919139594478
document id:    11062

document containing keyword(s): ['policies']
document score:  10.782919139594478
document id:    18734

document containing keyword(s): ['policies']
document score:  10.734172515171084
document id:     7310

document containing keyword(s): ['policies']
document score:  10.734172515171084
document id:    15525

document containing keyword(s): ['policies']
document score:  10.734172515171084
document id:    18086

document containing keyword(s): ['policies']
document score:  10.734172515171084
document id:    20868

document containing keyword(s): ['policies']
document score:  10.709964107818992
document id:    18130

document containing keyword(s): ['policies']
document score:  10.685864647527012
document id:    18299

document containing keyword(s): ['reform']
document score:  10.662308176727565
document id:    17477

document containing keyword(s): ['reform']
document score:  10.595725180160036
document id:     8203

document containing keyword(s): ['policies']
document score:  10.590541699073414
document id:    18357

document containing keyword(s): ['reform']
document score:  10.551796590806346
document id:      742

document containing keyword(s): ['policies']
document score:  10.543515137204317
document id:    18443

document containing keyword(s): ['reform']
document score:  10.508230742760672
document id:    17528

document containing keyword(s): ['policies']
document score:  10.496904365385536
document id:      181

document containing keyword(s): ['policies']
document score:  10.496904365385536
document id:    10661

document containing keyword(s): ['policies']
document score:  10.496904365385536
document id:    12471

document containing keyword(s): ['policies']
document score:  10.496904365385536
document id:    17119

document containing keyword(s): ['policies']
document score:  10.496904365385536
document id:    18681

document containing keyword(s): ['reform']
document score:  10.465023161480648
document id:     7610

document containing keyword(s): ['reform']
document score:  10.465023161480648
document id:    11320

document containing keyword(s): ['policies']
document score:  10.450703893513742
document id:     7314

document containing keyword(s): ['policies']
document score:  10.450703893513742
document id:     9788

document containing keyword(s): ['reform']
document score:  10.443552342665182
document id:     3030

document containing keyword(s): ['policies']
document score:  10.427755830771828
document id:    16759

document containing keyword(s): ['reform']
document score:  10.422169445715971
document id:     1957

document containing keyword(s): ['policies']
document score:  10.404908327717367
document id:     7031

document containing keyword(s): ['policies']
document score:  10.404908327717367
document id:     8176

document containing keyword(s): ['reform']
document score:  10.337506363261014
document id:    13323

document containing keyword(s): ['policies']
document score:  10.269898527838063
document id:     2223

document containing keyword(s): ['reform']
document score:  10.254207695345174
document id:    18403

document containing keyword(s): ['policies']
document score:  10.181821780613838
document id:    18005

document containing keyword(s): ['policies']
document score:  10.138347511194603
document id:    21391

document containing keyword(s): ['policies']
document score:  10.12393847130081
document id:    19508

document containing keyword(s): ['policies']
document score:  10.010124044217354
document id:     3928

document containing keyword(s): ['policies']
document score:  9.968100613920205
document id:    10255

document containing keyword(s): ['policies']
document score:  9.926428545100478
document id:    20461

document containing keyword(s): ['reform']
document score:  9.895394908735707
document id:    11175

document containing keyword(s): ['policies']
document score:  9.84412101146928
document id:     5542

document containing keyword(s): ['policies']
document score:  9.803476986877053
document id:    11600

document containing keyword(s): ['policies']
document score:  9.763167201233154
document id:     9442

document containing keyword(s): ['policies']
document score:  9.763167201233154
document id:    18148

document containing keyword(s): ['reform']
document score:  9.669818912800183
document id:     8038

document containing keyword(s): ['policies']
document score:  9.605189323298818
document id:    19947

document containing keyword(s): ['policies']
document score:  9.605189323298818
document id:    20805

document containing keyword(s): ['policies']
document score:  9.566490460749444
document id:     6796

document containing keyword(s): ['reform']
document score:  9.525062987472344
document id:    14826

document containing keyword(s): ['policies']
document score:  9.490020753310729
document id:    17394

document containing keyword(s): ['policies']
document score:  9.414763871820428
document id:     2197

document containing keyword(s): ['reform']
document score:  9.350100754615623
document id:     2118

document containing keyword(s): ['policies']
document score:  9.304090223126988
document id:    17296

document containing keyword(s): ['policies']
document score:  9.231742111361847
document id:     2913

document containing keyword(s): ['reform']
document score:  9.21469183930147
document id:    17443

document containing keyword(s): ['reform']
document score:  9.181450213168128
document id:    10670

document containing keyword(s): ['policies']
document score:  9.160510468150974
document id:    16200

document containing keyword(s): ['reform']
document score:  9.115681313791304
document id:    14880

document containing keyword(s): ['reform']
document score:  9.115681313791304
document id:    14911

document containing keyword(s): ['reform']
document score:  9.050847949319103
document id:     1954

document containing keyword(s): ['policies']
document score:  9.021294783064523
document id:     1969

document containing keyword(s): ['reform']
document score:  9.018775876843735
document id:    17038

document containing keyword(s): ['policies']
document score:  8.987149519498663
document id:     7025

document containing keyword(s): ['policies']
document score:  8.987149519498663
document id:    12856

document containing keyword(s): ['reform']
document score:  8.95530882595226
document id:     4940

document containing keyword(s): ['policies']
document score:  8.953261758388338
document id:     6039

document containing keyword(s): ['policies']
document score:  8.953261758388338
document id:     6744

document containing keyword(s): ['policies']
document score:  8.853114686749228
document id:     4871

document containing keyword(s): ['policies']
document score:  8.820228346406902
document id:     1947

document containing keyword(s): ['policies']
document score:  8.755183230497911
document id:    17269

document containing keyword(s): ['policies']
document score:  8.723019109187799
document id:      926

document containing keyword(s): ['policies']
document score:  8.69109044703464
document id:    12986

document containing keyword(s): ['reform']
document score:  8.680421907893857
document id:      308

document containing keyword(s): ['reform']
document score:  8.680421907893857
document id:     9659

document containing keyword(s): ['policies']
document score:  8.596691640977719
document id:    12415

document containing keyword(s): ['policies']
document score:  8.596691640977719
document id:    21119

document containing keyword(s): ['policies']
document score:  8.534890156228485
document id:    10134

document containing keyword(s): ['reform']
document score:  8.53487658780448
document id:     4815

document containing keyword(s): ['reform']
document score:  8.506351255064946
document id:    15369

document containing keyword(s): ['reform']
document score:  8.478015962362173
document id:     6410

document containing keyword(s): ['policies']
document score:  8.47397090894523
document id:    17058

document containing keyword(s): ['reform']
document score:  8.449868816888491
document id:     9873

document containing keyword(s): ['reform']
document score:  8.39413152125168
document id:      821

document containing keyword(s): ['reform']
document score:  8.39413152125168
document id:    17381

document containing keyword(s): ['policies']
document score:  8.384205346165736
document id:     9701

document containing keyword(s): ['policies']
document score:  8.384205346165736
document id:    13244

document containing keyword(s): ['reform']
document score:  8.325485478412705
document id:    20094

document containing keyword(s): ['policies']
document score:  8.325410778508022
document id:    14905

document containing keyword(s): ['policies']
document score:  8.325410778508022
document id:    20631

document containing keyword(s): ['reform']
document score:  8.28483414398067
document id:    20865

document containing keyword(s): ['policies']
document score:  8.2387489549634
document id:    10100

document containing keyword(s): ['policies']
document score:  8.210261223114399
document id:     7254

document containing keyword(s): ['policies']
document score:  8.210261223114399
document id:    11770

document containing keyword(s): ['policies']
document score:  8.210261223114399
document id:    18455

document containing keyword(s): ['reform']
document score:  8.204710901286608
document id:     1376

document containing keyword(s): ['reform']
document score:  8.152150866008943
document id:    19016

document containing keyword(s): ['reform']
document score:  8.049025462241241
document id:     5943

document containing keyword(s): ['reform']
document score:  7.99843501964103
document id:    17409

document containing keyword(s): ['policies']
document score:  7.962469445393546
document id:    12689

document containing keyword(s): ['reform']
document score:  7.9484765558685915
document id:     2541

document containing keyword(s): ['policies']
document score:  7.831163704708566
document id:    17300

document containing keyword(s): ['policies']
document score:  7.805420522143247
document id:    12942

document containing keyword(s): ['reform']
document score:  7.802276794923649
document id:     8069

document containing keyword(s): ['policies']
document score:  7.779846034831185
document id:    15191

document containing keyword(s): ['policies']
document score:  7.779846034831185
document id:    20756

document containing keyword(s): ['policies']
document score:  7.704118323902742
document id:     4575

document containing keyword(s): ['policies']
document score:  7.654446925821039
document id:     8676

document containing keyword(s): ['policies']
document score:  7.629850642855771
document id:    18328

document containing keyword(s): ['reform']
document score:  7.615509652344671
document id:     6431

document containing keyword(s): ['policies']
document score:  7.581129264967997
document id:     1210

document containing keyword(s): ['reform']
document score:  7.5702066624533515
document id:    16789

document containing keyword(s): ['reform']
document score:  7.525439480181654
document id:     7537

document containing keyword(s): ['reform']
document score:  7.481198655754226
document id:    19014

document containing keyword(s): ['policies']
document score:  7.346567090586821
document id:    12602

document containing keyword(s): ['reform']
document score:  7.330369515408742
document id:     5285

document containing keyword(s): ['policies']
document score:  7.301385723761298
document id:     6127

document containing keyword(s): ['policies']
document score:  7.147535101467228
document id:     7360

document containing keyword(s): ['policies']
document score:  7.126084134679758
document id:    16198

document containing keyword(s): ['policies']
document score:  7.062496876783232
document id:      263

document containing keyword(s): ['policies']
document score:  7.020732087646842
document id:    11387

document containing keyword(s): ['reform']
document score:  6.856427553655541
document id:    18420

document containing keyword(s): ['policies']
document score:  6.799577160153448
document id:     7628

document containing keyword(s): ['policies']
document score:  6.780161080444226
document id:     7032

document containing keyword(s): ['reform']
document score:  6.747365532618501
document id:    10605

document containing keyword(s): ['policies']
document score:  6.6847205377909225
document id:     3492

document containing keyword(s): ['policies']
document score:  6.610281147653993
document id:     8117

document containing keyword(s): ['policies']
document score:  6.501679511659432
document id:    16937

document containing keyword(s): ['reform']
document score:  6.391530611040447
document id:     6395

document containing keyword(s): ['reform']
document score:  6.3122712274951285
document id:     6472

document containing keyword(s): ['policies']
document score:  6.2948410955520115
document id:    11768

document containing keyword(s): ['policies']
document score:  6.031026056994713
document id:     8135

document containing keyword(s): ['reform']
document score:  6.028206360030109
document id:     7524

document containing keyword(s): ['reform']
document score:  5.9437389363152215
document id:     1226

document containing keyword(s): ['policies']
document score:  5.918283504848758
document id:    16963

document containing keyword(s): ['policies']
document score:  5.802579999325126
document id:    20863

document containing keyword(s): ['reform']
document score:  5.794875953789612
document id:      237

document containing keyword(s): ['reform']
document score:  5.781711866614095
document id:      226

document containing keyword(s): ['policies']
document score:  5.774357567426134
document id:     6351

document containing keyword(s): ['policies']
document score:  5.732534944447112
document id:    17216

document containing keyword(s): ['policies']
document score:  5.610624736959618
document id:     8076

document containing keyword(s): ['reform']
document score:  5.5911911506177985
document id:    17305

document containing keyword(s): ['policies']
document score:  5.481109947461842
document id:     1867

document containing keyword(s): ['policies']
document score:  5.35743964331894
document id:      179

document containing keyword(s): ['policies']
document score:  5.345378863001031
document id:     9795

document containing keyword(s): ['reform']
document score:  5.278123759218691
document id:    19015

document containing keyword(s): ['reform']
document score:  5.202599210140071
document id:    16214

document containing keyword(s): ['policies']
document score:  5.04980496889193
document id:      236

document containing keyword(s): ['policies']
document score:  5.007208859697289
document id:     3511

document containing keyword(s): ['policies']
document score:  4.8339149648761754
document id:    11881

document containing keyword(s): ['policies']
document score:  4.672214838229811
document id:    17368

document containing keyword(s): ['reform']
document score:  4.659672977710215
document id:     3562

document containing keyword(s): ['policies']
document score:  4.5644366539946875
document id:    13178

document containing keyword(s): ['policies']
document score:  4.529607145907163
document id:      874

document containing keyword(s): ['policies']
document score:  4.512390962461657
document id:    17017

document containing keyword(s): ['reform']
document score:  4.511013623018213
document id:    19543

document containing keyword(s): ['reform']
document score:  4.495079371792703
document id:     2427

document containing keyword(s): ['reform']
document score:  4.463546207598459
document id:    12025

document containing keyword(s): ['policies']
document score:  4.171506120881148
document id:     3019

document containing keyword(s): ['reform']
document score:  4.16412805313687
document id:    19291

document containing keyword(s): ['policies']
document score:  4.156900093994391
document id:     5850

document containing keyword(s): ['policies']
document score:  4.149635369453645
document id:    17201

document containing keyword(s): ['reform']
document score:  4.137053248009195
document id:     9758

document containing keyword(s): ['policies']
document score:  4.113689328960301
document id:    10995

document containing keyword(s): ['policies']
document score:  4.064398576418928
document id:    14766

document containing keyword(s): ['reform']
document score:  4.064381037013697
document id:    17358

document containing keyword(s): ['policies']
document score:  4.043633717605496
document id:    20027

document containing keyword(s): ['policies']
document score:  3.779723999835416
document id:     3064

document containing keyword(s): ['policies']
document score:  3.7498779504442683
document id:    13045

document containing keyword(s): ['reform']
document score:  3.719842995268889
document id:    11214

document containing keyword(s): ['policies']
document score:  3.6462270743265557
document id:    17293

document containing keyword(s): ['policies']
document score:  3.5694878710741214
document id:    16784

document containing keyword(s): ['reform']
document score:  3.543744328017887
document id:    19824

document containing keyword(s): ['policies']
document score:  3.455214960056311
document id:    14825

document containing keyword(s): ['policies']
document score:  2.661316320428642
document id:    17395
```