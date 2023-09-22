library(chorddiag)

data = read.csv("output_matrix.csv")
matrixdata = as.matrix(data)


# m <- matrix(c(11975,  5871, 8916, 2868,
#               1951, 10048, 2060, 6171,
#               8010, 16145, 8090, 8045,
#               1013,   990,  940, 6907),
#             byrow = TRUE,
#             nrow = 4, ncol = 4)


# A vector of 4 colors for 4 groups
countries <- c("black", "blonde", "brown", "red")
# 
# dimnames(m) <- list(have = haircolors,
#                     prefer = haircolors)
# groupColors <- c("#000000", "#FFDD89", "#957244", "#F26223")

# Build the chord diagram:
p <- chorddiag(m, groupColors = groupColors, groupnamePadding = 20)
p