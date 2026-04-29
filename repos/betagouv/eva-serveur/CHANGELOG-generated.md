## Changelog : eva-serveur (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur les aspects visuels avec l'adoption du Design System Français (DSFR) et la correction de nombreux problèmes d'affichage sur mobile. Des améliorations significatives ont également été apportées à la gestion des OPCO, des structures et des invitations, ainsi qu'à la gestion des évaluations et de leurs restitutions. Des corrections de sécurité et des refactorisations techniques ont également été réalisées.

### Évolutions fonctionnelles
- Les tableaux d'évaluation utilisent désormais le design DSFR.
- Amélioration de la gestion des invitations : ajout d'une page dédiée pour les invitations invalides, amélioration des alertes et du parcours d'inscription.
- Les OPCO peuvent désormais accéder à un dashboard avec des statistiques Metabase.
- Possibilité pour les comptes OPCO d'accéder à leur dashboard avec les statistiques Metabase.
- Ajout de la gestion des parcours types pour les OPCO, permettant de lier des parcours spécifiques à chaque opérateur de compétences.
- Amélioration de la gestion des structures lors de l'inscription, notamment en cas de doublon de SIRET.
- Les administrateurs peuvent modifier leur structure même si le SIRET est en doublon.
- Les super-admins peuvent créer des structures sans SIRET.
- Amélioration de la restitution des évaluations, avec l'ajout des 8 étapes des incontournables pour les professionnels.
- Distinction des exports XLS pour les évaluations EVA et EVA Pro.
- Possibilité de consulter les explications de comparaison des évaluations littératie et numératie.
- Ajout d'une fonctionnalité d'invitation pour les structures administratives.
- Les utilisateurs peuvent maintenant consulter les pistes de solutions disponibles renvoyant vers le widget de l'inclusion.
- Amélioration de la gestion des fichiers audio dans les transcriptions avec une validation de l'extension.

### Évolutions techniques
- Refactorisation de la gestion des évaluations avec l'introduction des classes `DiagnosticPro` et `PassationBeneficiaire` pour une meilleure structuration du code.
- Migration du script I18n vers une dépendance npm.
- Suppression des utilities Bootstrap au profit du DSFR.
- Suppression de nombreuses références à Bootstrap et remplacement par des composants DSFR.
- Amélioration de la performance avec la mise en cache de libvips dans la CI.
- Correction d'une vulnérabilité d'injection SQL dans `CollectionsEvenementsController`.
- Correction d'une faille de sécurité sur TarteauCitronJS.
- Mise à jour de Ruby et Nodejs.
- Refactorisation du code pour utiliser `evapro?` au lieu de `evaluation_evapro?`.
- Amélioration de la gestion des mises en action dans le modèle `Evaluation`.
- Correction d'un N+1 sur la page des actualités.
- Utilisation de l'API geo.api.gouv.fr pour la géolocalisation des structures.
- Ajout de tests pour la méthode `departement` de `geoloc_helper`.

### Autres changements
- Ajout de styles pour l'impression et ajustement de la génération de PDF.
- Correction de l'intégration des actualités et du bouton menu des actualités.
- Suppression du numéro de téléphone de Gaelle.
- Correction de bugs d'affichage et de style sur mobile.
- Correction de padding et de marges inutiles.
- Amélioration de la documentation et des commentaires.
- Suppression de code obsolète.
- Mise à jour de dépendances (hors mises à jour de routine).
- Configuration de Plausible pour tracer les liens sortants.
- Harmonisation du wording « rejoindre une structure existante ».
- Correction de l'URL des restitutions Eva Pro.
- Correction de l'affichage des campagnes dans le dashboard Eva Pro.
- Correction des warnings lint.
- Ajout de validations et de tests unitaires.
- Amélioration de la gestion des erreurs.
- Correction de la redirection pour les comptes ProConnect sans structure.
- Ajout de la gestion de l'usage et de l'OPCO pour les structures administratives.
- Ajout de la possibilité de créer une campagne à la création d'une structure.
- Ajout d'une table de liaison entre OPCO et parcours type.
- Correction du visuel des actualités.
- Suppression du captcha sur certaines pages.
- Ajout de la gestion de la suppression d'images dans les formulaires.
- Ajout de la gestion de la suppression dans le file input.
- Amélioration de l'affichage des boutons du header en version mobile.
- Correction du background hover du header DSFR.
- Correction des boutons du header version mobile.
- Correction du padding left des radio button d'activeadmin.
- Correction du padding left des commentaires dans les pages détails d'activeadmin.
- Correction de la classe mx-auto.
- Correction du padding des labels des forms.
- Ajout du logo evapro dans la démonstration.
- Ajout de padding sur la version mobile du tableau des evaluations eva.
- Ajout du logo de l'opco dans le header du pdf uniquement si il est financeur.
- Changement des wording des risques dans les restitutions.
- Changement du wording de l'item "Parcours" par "Parcours type" dans le header.
- Correction du hover du breadcrumb.
- Correction de la page structure en mobile.
- Correction de la modale du tableau de bord sur mobile.
- Correction du détail d'une actualité sur mobile.
- Correction de la page mon compte sur mobile.
- Correction du rendu du mobile pour la page aide.
- Correction de l'interface de la page actualités sur mobile.
- Correction de la modale d'invitation sur mobile.
- Correction du breadcrumb sur mobile.
- Correction de la page détail d'un bénéficiaire sur mobile.
- Correction de la page Ma structure.
- Correction de la page aide.
- Correction de la page mon compte.
- Correction de la page Ma structure.
- Correction de la page structure en mobile.
- Correction de la modale d'invitation.
- Correction de la page d'édition de ma structure sur mobile.
- Correction de l'intégration des actualités.
- Correction de l'utilisation de fr-sr-only du DSFR.
- Correction d'un bug sur les select dans les filtres d'activeadmin.
- Correction de la classe mx-auto.
- Correction du padding inutile dans les filtres.
- Correction du tableau Evaluation eva.
- Correction du padding bottom pour les labels des forms.
- Correction de la version petit ecran.
- Correction de la version pdf.
- Correction de l'erreur 500 sur la page index Questionnaires.
- Ajout du logo de l'opco dans le header du pdf uniquement si il est financeur.
