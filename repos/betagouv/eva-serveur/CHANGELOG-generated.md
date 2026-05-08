## Changelog : eva-serveur (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la gestion des structures, notamment des opérateurs de compétences (OPCO), et sur l'amélioration de l'expérience utilisateur, en particulier sur la gestion des accès et l'affichage des données. Des corrections de bugs et des améliorations de la performance ont également été apportées.

### Évolutions fonctionnelles
- Permet d'accéder à la liste des structures Operateurs de compétences. [#fd6c11b](https://github.com/betagouv/eva-serveur/issues/fd6c11b)
- Ajout d'un dashboard pour les comptes OPCO avec les statistiques Metabase associées.
- Possibilité de créer ou modifier une structure Opérateur de compétences.
- Permet d'accéder au show d'une structure Opérateur de compétence.
- Les pistes de solutions disponibles renvoient vers le widget de l'inclusion.
- Amélioration de la gestion des invitations et des comptes en attente.
- Permet de consulter les explications de comparaison des évaluations littératie et numératie.
- Ajout de la fonctionnalité d'invitation pour les structures administratives.
- Les utilisateurs OPCO ont un accès restreint à la navigation d'EVA.
- Permet de ne pas scroller en dehors des modales et de continuer à naviguer au clavier dans les modales.
- Permet de consulter les 8 étapes des incontournables dans la restitution pour les pros.
- Permet d'enregistrer le numéro de téléphone lors de la création d'un compte lors de l'embarquement.

### Évolutions techniques
- Refactor de la logique de formatage du SIRET pour éviter les duplications de code et améliorer la maintenabilité. [#8821b19](https://github.com/betagouv/eva-serveur/issues/8821b19)
- Remplacement de Nominatim par geo.api.gouv.fr pour la géolocalisation des structures, améliorant la fiabilité et la conformité.
- Suppression de la librairie `geocoder` et des fonctionnalités associées à la recherche de structures par code postal.
- Suppression des pages et fonctionnalités liées à la création et à la recherche de structures.
- Utilisation du validateur blob d’ActiveStorage pour valider le type audio des transcriptions.
- Migration des fichiers de migration de 2025 dans un dossier dédié.
- Mise à jour de Ruby et Nodejs.
- Suppression des utilities Bootstrap au profit du DSFR.
- Correction d'une vulnérabilité d'injection SQL dans CollectionsEvenementsController.
- Correction d'une faille de sécurité sur TarteauCitronJS.
- Amélioration de la configuration de Plausible pour le suivi des liens sortants.
- Amélioration du cache de libvips dans la CI.
- Refactor de la logique de calcul de la complétude des évaluations EVAPRO.
- Utilisation du StatistiquesStructure pour l'intégration des statistiques Metabase OPCO.

### Autres changements
- Correction de plusieurs problèmes de style et d'affichage, notamment sur les pages mobiles et les PDF.
- Suppression de code mort et de configurations inutiles.
- Ajout de tests unitaires et correction de tests existants.
- Amélioration de la documentation et des commentaires dans le code.
- Correction de plusieurs erreurs de linting.
- Suppression du numéro de téléphone de Gaelle.
- Mise à jour de certaines dépendances.
- Correction des références à 'focus-incoutournable' en 'focus-incontournable'.
- Renommage de l'usage 'Eva: entreprises' en 'EVAPRO'.
- Correction du titre de la sidebar :responsable_de_suivi.
- Suppression du code de l'ancien menu mobile.
- Correction de l'affichage des évaluations EVAPRO incomplètes.
- Correction des URL des restitutions EVA Pro.
- Ajout d'un padding sur la version mobile du tableau des évaluations EVA.
- Correction des marges entre le Header/Contenu et Contenu/footer sur l'ensemble des pages.
- Correction du focus des boutons DSFR sur Firefox.
- Correction du bug des accès.
- Correction des comptes en attente dans /comptes.
- Correction de l'alignement des cards diagnostique sur le dashboard.
- Correction du problème d'affichage sur les restitutions EVA.
- Correction des classes bootstrap des utilities qui n'ont pas été converties pour utiliser le DSFR.
- Correction des bulles vertes collées aux titres des situations.
- Correction des erreurs 500 sur la page index Questionnaires.
- Correction des erreurs de padding et de marges sur les pages.
- Suppression des progress bar de bootstrap.
- Suppression du background des forms.
- Ajout de tests pour la méthode departement de geoloc_helper.
- Ajout d'un test pour vérifier le bouton menu des actualités.
- Ajout d'un test pour la méthode vue_opco_active?.
- Correction des liens d'invitation avec structure_id.
- Suppression de l'action rejoindre_structure.
- Suppression de la page 'structures'.
- Suppression de l'étape de prise en main 'Recherche structure'.
- Suppression du bouton bouton_ajouter_une_structure.
- Suppression de la page admin/recherche_structure.
- Suppression de la page 'nouvelle_structure'.
- Suppression de la page 'admin/sign_up'.
- Ajout de mailers/structure/invitation_structure.
- Assigne l'etape d'inscription quand on crée un compte avec l'admin.
- Linter sur un fichier css.
- Vide les comptes créés en démo, même invités.
- Change les invitations en attente.
- Corrige les invitations en attente.
- Corrige la redirection pour les comptes ProConnect sans structure.
- Corrige les comptes en attente dans /comptes.
