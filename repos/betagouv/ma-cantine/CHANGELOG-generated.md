## Changelog : ma-cantine (30 derniers jours)

### Résumé
Les dernières mises à jour de ma-cantine apportent des améliorations significatives à l'import de données, notamment pour les bilans détaillés et les cantines. Des corrections de bugs ont également été implémentées, ainsi que des optimisations techniques et des mises à jour de dépendances pour assurer la stabilité et la performance de la plateforme. De nouvelles fonctionnalités ont été ajoutées pour faciliter l'export de données et la gestion des cantines.

### Évolutions fonctionnelles
- Ajout d'une nouvelle fonctionnalité permettant d'importer des bilans via l'ID de la cantine.
- Nouvelle page dédiée à l'import de bilans détaillés avec un schéma compatible Validata.
- Possibilité d'exporter la liste des cantines au format xlsx.
- Ajout de la possibilité d'exporter les cantines enregistrées via SIREN.
- Suppression du bandeau d'alerte rappel conso dans l'en-tête.
- Amélioration des messages d'erreur lors de l'import de fichiers (cantines et bilans) en cas d'en-tête incorrecte.
- Ajout de supports webinaire pour les acteurs de terrain et les cuisines centrales/satellites.
- Mise à jour de l'antisèche et du kit du télédéclarant.

### Évolutions techniques
- Mise à jour de Django de 5.1.15 à 5.2.11, incluant également les mises à jour de DRF et Wagtail.
- Simplification des exports secteur et catégorie, avec correction de l'export Metabase.
- Amélioration des performances de l'API de liste des achats (avec/sans filtres).
- Refactor de l'API de recherche d'entreprises pour récupérer les informations d'état administratif et de date de fermeture.
- Utilisation de services dédiés pour Postgres et Redis dans les tests.
- Amélioration de la gestion des données géographiques des cantines (récupération en temps réel).
- Suppression de l'import admin pour les cantines.
- Suppression du champ déclaratif "satellite_canteens_count".
- Modification de l'emplacement des fichiers d'import pour les cantines.
- Ajout de tests pour expliciter le fonctionnement des historisations.
- Amélioration de la gestion des champs de lecture seule dans l'admin des cantines.
- Suppression des emails de rappels 'pas de diagnostics' et bascule sur Brevo.
- Stockage des données de bilans dans le champ 'data' pour Brevo.
- Mise à jour des informations cantines plus tôt dans la nuit pour Brevo.
- Correction d'un bug empêchant le calcul correct des totaux EGalim.
- Correction d'un bug lié à l'exclusion des TD groupes des calculs TD.
- Correction d'une erreur bloquante dans le tableau de bord si une cantine n'a pas de mode de production.
- Correction d'un bug lié à l'annulation des télédéclarations.
- Correction d'un bug lié aux liens vers les fichiers d'exemple.
- Correction d'un bug lié à la vérification des champs de cantine lors de la revendication.
- Correction d'une erreur sur les prix lors de l'import des achats.
- Amélioration de la verbose_name des champs dans le diagnostic.
- Ajout de règles métier sur le ministère de tutelle.
- Ajout de nouveaux imports cantines dans les erreurs à ignorer dans Sentry.
- Mise à jour des textes de la page tampon.

### Autres changements
- Ajout d'instructions pour Claude et Github Copilot.
- Documentation mise à jour concernant la télédéclaration.
- Ajout de commentaires et d'informations dans le code pour faciliter la maintenance.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration des tests unitaires.
- Mise à jour des fichiers d'export Open Data.
- Ajout de la version de la télédéclaration dans les exports Metabase.
- Homogénéisation des tests entre Metabase et Open Data pour les cantines et les télédéclarations.
- Ajout d'une nouvelle propriété pour détecter les cantines avec des données géographiques manquantes.
- Amélioration de la gestion des données géo dans les tests.
