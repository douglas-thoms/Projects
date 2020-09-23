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

#new goal - 10 peak table comparison, can chose actual or forecast

# Define UI for application that draws a histogram
shinyUI(
                
        
        
        dashboardPage(
                dashboardHeader(title="Controls"),
                dashboardSidebar(
                        
                        menuItem(selectInput("iso", "Choose an ISO:",
                                                        c("ISONE" = "ISONE",
                                                          "NYISO" = "NYISO",
                                                          "PJM" = "PJM"))),
                        menuItem("Select parameters for table"),
                                menuSubItem(selectInput("year", "Year:",
                                                        c("2017" = "2017",
                                                          "2018" = "2018",
                                                          "2019" = "2019",
                                                          "2020" = "2020"))),
                        
                                menuSubItem(numericInput("num", "Number of peaks", 
                                                         10, min = 1, max = 20)),
                        
                        
                                menuSubItem(selectInput("forecaster", "Forecaster:",
                                                        c("Enverus" = "enverus",
                                                          "Genscape" = "genscape")))
                        


                                
                ),
                dashboardBody(
                        fluidPage( titlePanel("US Markets"),
                                fluidRow(
                                        box(plotOutput("barplot1")),
                                        box(plotOutput("barplot2"))
                                ),
                                
                                fluidRow(
                                        dataTableOutput('table'))
                        
                        )

       )

   )
   
)