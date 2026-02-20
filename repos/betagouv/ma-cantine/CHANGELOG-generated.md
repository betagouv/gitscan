## Changelog : ma-cantine (30 derniers jours)

### Résumé
Les dernières mises à jour de ma-cantine se concentrent sur l'amélioration des fonctionnalités d'import de données, notamment pour les bilans et les cantines, ainsi que sur l'ajout de nouvelles ressources pour les utilisateurs. Des optimisations techniques ont également été apportées pour améliorer les performances et la maintenance du code.

### Évolutions fonctionnelles
- Ajout d'un nouvel import de bilans via l'ID de la cantine (#6393).
- Nouvelle page dédiée aux imports de bilans détaillés (#6397).
- Suppression de l'import admin pour les cantines (#6387).
- Création d'un fichier d'import pour les gestionnaires de cantines uniquement (#6383).
- Correction d'un bug empêchant la revendication d'une cantine si des champs étaient vérifiés incorrectement (#6388).
- Correction d'un bug sur les prix lors de l'import des achats (#6389).
- Suppression du bandeau rappel conso dans l'en-tête (#6384).
- Ajout de supports et de résultats de webinaires concernant la gestion des cantines concédées et des cuisines centrales/satellites (#6377, #6350, #6302).
- Ajout du kit du télédéclarant (#6309).
- Mise à jour de l'antisèche et du kit du télédéclarant (#6346).
- Ajout d'une modale d'export sur le tableau de bord (#6368).
- Ajout d'un endpoint API pour générer la liste des cantines au format xlsx (#6369).
- Amélioration du wording des caractéristiques "performance" et "externalités" dans les achats (#6342).

### Évolutions techniques
- Refactor de la gestion des tests pour les imports de bilans simples (#6392).
- Réparation d'un test suite aux récentes modifications géographiques (#6385).
- Mise à jour des informations de version dans la documentation de la télédéclaration (#6401).
- Mise en place de services dédiés pour Postgres et Redis dans les tests (#6380).
- Ajout de deux nouveaux champs (siret_ et date_fermeture) pour gérer les informations sur le statut du SIRET des cantines (#6376, #6375).
- Simplification de l'export Open Data des cantines en gérant le line_ministry dans le serializer (#6354).
- Suppression de fonctions Metabase non utilisées (#6353).
- Amélioration des performances de l'API de liste des achats (#6364).
- Suppression de la vérification des données géographiques lors des imports de cantines, car elles sont maintenant récupérées à la création (#6363).
- Amélioration des mocks pour les tests des API de recherche d'entreprises et de découpage administratif (#6286, #6284).
- Refactor de la gestion des tâches nocturnes pour mettre à jour les informations des cantines plus tôt (#6366).
- Homogénéisation des tests entre Metabase et Open Data pour les télédéclarations et les cantines (#6321, #6308, #6305).
- Basculement des emails de rappel "pas de diagnostics" de Django vers Brevo (#6282).
- Stockage des données de bilan des cantines dans le champ 'data' pour Brevo (#6367).
- Amélioration de l'export des colonnes PAT dans les exports Open Data (#6322).

### Autres changements
- Mise à jour de la documentation d'onboarding (#6357).
- Correction du calcul des totaux EGalim avec les valeurs performances et environnalités (#6362).
- Correction d'un bug empêchant l'affichage correct de l'input de gaspillage alimentaire (#6377).
- Correction d'une redirection incorrecte après la création de compte (#6376).
- Ajout d'un bandeau d'alerte pour le rappel des laits infantiles (#6312).
- Mise à jour de la convention de délégation (#6301).
- Ajout d'une règle métier sur le ministère de tutelle des cantines (#6319).
- Renommage d'une colonne dans l'import des cantines (#6261).
