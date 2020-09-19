#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
shinyUI(
        dashboardPage(
                dashboardHeader(title="US Market"),
                dashboardSidebar(
                        
                        menuItem("ISO"),
                                menuSubItem(selectInput("iso", "Choose an ISO:",
                                                        c("ISONE" = "ISONE",
                                                          "NYISO" = "NYISO",
                                                          "PJM" = "PJM")))

                                
                ),
                dashboardBody(
                        fluidRow(
                                box(plotOutput("barplot1")),
                        fluidRow(
                                box(plotOutput("barplot2"))
                        )
                )
        )

        )

)