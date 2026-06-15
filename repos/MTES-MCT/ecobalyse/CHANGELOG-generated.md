## Changelog : ecobalyse (30 derniers jours, au 11 juin 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement de la base de données avec de nouveaux matériaux et processus, notamment dans les domaines des batteries, de l'emballage et de l'alimentation. Des améliorations ont également été apportées à la gestion des transports, des distances et des calculs, ainsi qu'à la fiabilité des tests et de l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout de composants de batterie (NMC622, AA, AAA) et de processus associés. [#2406]
- Intégration de nouveaux matériaux d'emballage : bois, papier, PET différencié. [#2376, #2404]
- Ajout de données pour le transport de marchandises depuis le Maroc. [#2144]
- Amélioration de la gestion des compléments alimentaires et de leur hiérarchie. [#2027]
- Possibilité d'indiquer si un composant est recyclable. [#2229]
- Ajout de données pour les céréales et les légumineuses cuisinés. [#2402]
- Ajout de données pour la cuisson au gaz. [#2211]
- Publication de la section réglementaire pour l'alimentation. [#2312]
- Ajout de composants pour les batteries (assemblage). [#2362]
- Ajout de processus pour les batteries (recyclage). [#2292]
- Ajout de données pour le verre feuilleté. [#2403]
- Ajout de données pour le polyester non tissé. [#2421]
- Ajout de données pour les pneus en tant que processus. [#2415]

### Évolutions techniques
- Refactorisation pour permettre l'absence d'impacts par défaut, avec une valeur de zéro. [#2417]
- Amélioration de la fiabilité des tests E2E en évitant les tentatives répétées. [#2422]
- Correction de la gestion des distances intra-pays. [#2301]
- Mise à jour des dépendances npm et yarn. [#2330, #2341, #2389, #2276]
- Amélioration de la gestion des transports aériens. [#2377]
- Correction de la gestion des données JSON pour les composants. [#2393]
- Correction de la gestion des ratios de transport pour les distances par défaut. [#2307]
- Amélioration de la gestion des erreurs lors de la récupération des impacts. [#2353]
- Utilisation de JSON pour stocker les composants. [#2393]

### Autres changements
- Affichage de l'alias dans l'explorateur. [#2444]
- Ajout d'un ADR pour la gestion de la localisation des composants. [#1900]
- Correction de l'affichage du nom des processus d'assemblage de batterie. [#2375]
- Suppression de processus obsolètes. [#2311]
- Correction du type de matériau des fibres PET recyclées. [#2365]
- Ajout de facteurs de complément pour les forêts. [#2391]
- Correction d'un bug de régression dans l'alimentation. [#2318]
- Ajout d'impacts pour la cuisson. [#2284]
- Restauration des origines d'outre-mer dans les données. [#2334]
- Exclusion du dossier de données de l'image Scalingo. [#2300]
- Correction de la configuration CI. [#2297]
- Mise à jour de la base de données browserslist. [#2407]
