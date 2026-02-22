## Changelog : ma-cantine (30 derniers jours)

### Résumé
Les dernières mises à jour de ma-cantine se concentrent sur l'amélioration des fonctionnalités d'import de données, notamment pour les cantines et les bilans, avec l'ajout de nouveaux schémas et d'options d'import par identifiant. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour l'export de données et la gestion des cantines, ainsi que des corrections de bugs pour assurer une meilleure stabilité et une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les cantines enregistrées via SIREN (#6409).
- Suppression du bandeau d'alerte "rappel conso" dans l'en-tête (#6384).
- Nouvelle page dédiée à l'import de bilans détaillés avec un schéma compatible Validata (#6397, #6394).
- Possibilité d'importer des bilans via l'ID de la cantine (#6393).
- Création d'un fichier d'import dédié aux gestionnaires de cantines (#6383).
- Création de fichiers dédiés pour la création et la modification des cantines (#6407, #6395).
- Suppression de l'import admin pour les cantines (#6387).
- Mise à jour des textes de la page tampon pour les imports (#6411).
- Ajout de supports webinaires sur la gestion concédée (#6377).
- Ajout du kit du télédéclarant et des supports webinaires sur les cuisines centrales et satellites (#6355, #6350, #6302).
- Ajout d'une modale d'export sur le tableau de bord (#6368).
- Ajout d'un nouvel endpoint API pour générer la liste des cantines en XLSX (#6369).

### Évolutions techniques
- Refactor de la gestion des imports de bilans simples pour préparer les imports de bilans détaillés (#6392).
- Amélioration des performances de l'API de statistiques en incluant les TD groupes (#6399).
- Correction d'une erreur bloquante sur le tableau de bord si une cantine n'a pas de mode de production (#6410).
- Correction d'une erreur sur les prix lors de l'import des achats (#6389).
- Amélioration de la gestion des données géographiques des cantines, avec récupération en temps réel (#6266).
- Mise à jour des informations des cantines plus tôt dans la nuit pour Brevo (#6366).
- Amélioration des performances de l'API des achats (#6364).
- Simplification de l'export Open Data des cantines en utilisant les données déjà stockées en base de données (#6307).
- Refactor de l'API de recherche d'entreprises et de découpage administratif pour améliorer les tests (#6286, #6284).
- Ajout de services dédiés pour Postgres et Redis dans les tests CI/CD (#6380).
- Utilisation de caches pour optimiser les appels à l'API PATs (#6263).

### Autres changements
- Ajout d'informations dans le tableau des versions de la télédéclaration (#6401).
- Ajout de tests pour expliciter le fonctionnement des historisations (#6295).
- Correction de liens et de tests suite à des modifications récentes (#6385, #6404).
- Ajout de règles métier sur le ministère de tutelle des cantines (#6319).
- Amélioration du wording pour les caractéristiques des achats (performance et externalités) (#6342).
- Mise à jour de la documentation d'onboarding (#6357).
- Correction de la vérification des totaux EGalim dans la télédéclaration (#6362).
- Correction du non affichage d'un input dans la gestion du gaspillage alimentaire (#6377).
- Correction de la redirection après la création de compte (#6276).
- Suppression de certains champs inutilisés dans Metabase (#6353).
- Amélioration de l'affichage des champs dans l'admin Django (#6363, #6291, #6269).
- Ajout de fieldsets pour organiser les champs dans l'admin des cantines (#6363).
- Ajout de la possibilité de filtrer les cantines par groupes dans l'admin (#6267).
- Amélioration de l'export des colonnes PATs dans Open Data (#6322).
- Mise à jour des annexes du protocole de pesées (#6272).
- Correction du calcul des totaux EGalim (#6362).
- Ajout de tests pour les exports de télédéclaration (#6308).
- Amélioration de l'export des fichiers Open Data (#6354).
- Correction d'un bug empêchant la revendication d'une cantine si des champs étaient vérifiés (#6388).
- Ajout de la gestion des cantines fermées ou avec SIRET inconnu (#6376).
- Amélioration de la gestion des erreurs dans les imports (#6278, #6323).
- Suppression du bandeau d'alerte sur les laits infantiles (#6384).
