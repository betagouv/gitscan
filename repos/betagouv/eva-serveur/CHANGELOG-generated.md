## Changelog : eva-serveur (30 derniers jours, au 8 mai 2026)

### Résumé
Ce mois-ci, les évolutions d'eva-serveur se concentrent sur l'amélioration de la gestion des structures, notamment des opérateurs de compétences (OPCO), et sur l'expérience utilisateur. Des corrections de bugs et des améliorations de l'interface ont été apportées, ainsi que des optimisations techniques pour la géolocalisation et la sécurité.

### Évolutions fonctionnelles
- Ajout d'un filtre par SIRET pour la recherche de structures.
- Possibilité de rechercher un SIRET avec des espaces.
- Les comptes créés en démo peuvent être vidés même s'ils ont été invités.
- Permet d'accéder à la liste des structures Opérateurs de compétences.
- Les utilisateurs OPCO peuvent accéder à leur dashboard avec les statistiques Metabase.
- Ajout de la gestion de l'usage et de l'OPCO pour les structures administratives.
- Permet de consulter les explications de comparaison des évaluations littératie et numératie.
- Les pistes de solutions disponibles renvoient vers le widget de l'inclusion.
- Ajout de la fonctionnalité d'invitation pour les structures administratives.
- Permet de consulter les restitutions EVA Pro.
- Ajout de la possibilité pour les employés d'OPCO d'avoir un accès restreint à la navigation d'EVA.
- Les évaluations EVA Pro incomplètes s'affichent correctement.
- Ajout d'un nouveau modèle StructureOpco pour gérer les opérateurs de compétences.
- Possibilité de créer ou de modifier une structure Opérateur de compétence.
- Accès au show d'une structure Opérateur de compétence.

### Évolutions techniques
- Remplacement de Nominatim par geo.api.gouv.fr pour la géolocalisation des structures, améliorant la précision et la fiabilité.
- Refactor de la logique de formatage du SIRET pour éviter les duplications de code.
- Suppression de la librairie `geocoder` et des pages associées à la recherche de structure par code postal.
- Suppression de l'action `rejoindre_structure` et de la page 'structures'.
- Suppression de la page 'nouvelle_structure'.
- Amélioration de la gestion des invitations en attente.
- Utilisation du validateur blob d’ActiveStorage pour valider le type audio des transcriptions.
- Mise à jour de Ruby et Nodejs.
- Correction d'une vulnérabilité d'injection SQL dans CollectionsEvenementsController.
- Correction d'une faille de sécurité sur TarteauCitronJS.
- Configuration de Plausible pour tracer les liens sortants.
- Refactor de la logique de calcul de la complétude des évaluations EVA Pro.
- Amélioration de la CI avec mise en cache de libvips et augmentation des timeouts.

### Autres changements
- Correction de l'affichage des bulles vertes collées aux titres des situations.
- Correction de l'affichage des restitutions EVA.
- Correction du focus des boutons DSFR sur Firefox.
- Correction des classes bootstrap remplacées par le DSFR.
- Correction de l'alignement des cards diagnostique sur le dashboard.
- Correction de bugs d'affichage sur mobile (page Ma structure, actualités, compte, aide, etc.).
- Correction de problèmes de style et de padding sur diverses pages.
- Ajout de tests unitaires pour certaines fonctionnalités.
- Suppression de code mort et de fichiers inutiles.
- Amélioration de la documentation et des commentaires.
- Correction de plusieurs erreurs Rubocop.
- Ajout de la gestion des liens d'invitation avec l'ID de structure.
- Ajout d'un nouveau mailer pour les invitations de structure.
- Suppression de la page 'admin/sign_up'.
- Ajout d'un helper pour le formatage du SIRET.
- Suppression du bouton 'ajouter une structure'.
- Suppression de la page 'admin/recherche_structure'.
- Suppression de l'étape de prise en main 'Recherche structure'.
- Ajout d'une migration pour créer les StructureOpco via les StructureAdministrative.
- Ajout du bon layout et Header pour les comptes opco.
- Suppression du code mort concernant le rattachement des structures administratives à un OPCO.
- Utilisation de StatistiquesStructure pour l'intégration des statistiques Metabase OPCO.
- Suppression des traits inutiles dans les factory de structures.
- Renommage de la méthode `vue_opco_active?` en `utilisateur_opco?`.
- Correction de l'affichage des actualités.
- Correction de l'affichage des évaluations EVA.
- Correction du bug des accès.
- Ajout de styles pour l'impression et ajustement de la génération de PDF.
- Tous les tableaux sont passés en `dsfr_table`.
- Correction de l'url des restitutions EVA Pro.
- Correction des marges entre le Header/Contenu et Contenu/footer sur l'ensemble des pages.
- Ajout du logo de l'opco dans le header du pdf uniquement si il est financeur.
- Ajustement du design du PDF de comparatifs bénéficiaire en DSFR.
- Correction de la version petit écran.
- Correction de la version pdf.
- Le pro peut prendre connaissance des 8 étapes des incontournables dans sa restitution.
- Ajout de la possibilité de vider les comptes créés en démo, même invités.
- Correction de l'assignation de l'étape d'inscription lors de la création d'un compte par l'admin.
- Ajout d'un test pour la méthode `departement` de `geoloc_helper`.
- Correction de la purge des comptes référencés dans des invitations.
- Correction du double soulignement du lien de l'email dans la recherche de structure dans l'onboarding.
- Ajout du code commune dans la table structure.
- Enregistrement du code_commune à la création d'une structure.
- Correction du scroll horizontal sur les pages listes evapro (vues admin).
- Correction de la redirection pour les comptes ProConnect sans structure.
- Correction de la version mobile du contact opco dans l'évaluation.
- Correction de l'affichage des actualités.
- Correction du visuel des actualités.
- Correction du bug des accès.
- Correction de la modale d'invitation.
- Correction du breadcrumb.
- Correction du détail d'un bénéficiaire.
- Correction de l'interface de la page actualités.
- Correction de la modale d'invitation.
- Correction de la page mon compte.
- Correction de la page aide.
- Correction de la page structure.
- Correction de la page Ma structure.
- Correction de l'index des comptes sur EvaPro.
- Correction du padding left des radio button d'activeadmin.
- Correction du padding left des commentaires dans les pages détails d'activeadmin.
- Correction de la classe mx-auto.
