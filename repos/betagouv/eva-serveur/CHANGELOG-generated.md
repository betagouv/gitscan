## Changelog : eva-serveur (30 derniers jours, au 17 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment la migration vers le Design System Fr (DSFR) pour une cohérence visuelle accrue. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des évolutions concernant la gestion des structures, des utilisateurs et des évaluations, en particulier pour les offres Eva Pro.

### Évolutions fonctionnelles
- Permet de consulter les explications de comparaison des évaluations littératie et numératie.
- Les pistes de solutions disponibles renvoient vers le widget de l'inclusion.
- Les admins peuvent maintenant créer des structures sans SIRET.
- Ajout d'une page dédiée pour les invitations invalides.
- Possibilité de distinguer les exports XLS des évaluations Eva et Eva Pro.
- Les super-admins peuvent modifier les IDCC (identifiants conventions collectives) d’un OPCO.
- Possibilité de supprimer le visuel de l'offre de services dans le modèle Opco.
- Amélioration de l'affichage de l'index des évaluations pour EvaPro.
- Ajout de la gestion des comptes en attente restreints dans le composant de navigation.
- Amélioration de la gestion des structures lors de l'inscription, notamment en cas de doublon de SIRET.
- Ajout du code commune dans la table structure et enregistrement à la création.
- Géolocalisation des structures via geo.api.gouv.fr.
- Les utilisateurs peuvent désormais consulter les explications de comparaison des évaluations littératie et numératie.
- Amélioration de la navigation et de l'affichage des alertes dans le parcours d'inscription.

### Évolutions techniques
- Migration progressive de l'interface utilisateur vers le Design System Fr (DSFR), remplaçant les composants Bootstrap.
- Refactorisation du code pour améliorer la structure et la cohérence, notamment dans les contrôleurs et les modèles.
- Mise à jour des dépendances (Rails, ActiveAdmin, Devise).
- Amélioration de la gestion des erreurs et des validations.
- Optimisation de la performance de l'affichage de l'index des évaluations EvaPro.
- Mise en cache de libvips pour améliorer la performance de la CI.
- Configuration de Plausible pour tracer les liens sortants.
- Anonymisation du SIRET des structures supprimées et des bénéficiaires.
- Refactorisation de la gestion des mises en action dans le modèle `Evaluation` avec l'introduction de la classe `PassationBeneficiaire`.
- Utilisation de classes dédiées pour la gestion des risques et des coûts dans le modèle `DiagnosticPro`.

### Autres changements
- Correction de bugs mineurs concernant l'affichage des boutons, des liens, des marges et des modals.
- Amélioration de la documentation et des commentaires dans le code.
- Corrections de fautes de frappe et d'erreurs de wording.
- Ajout de tests unitaires et d'intégration pour valider les nouvelles fonctionnalités et les corrections de bugs.
- Suppression de code obsolète et de fichiers inutilisés.
- Ajustement des styles et de la mise en page pour une meilleure expérience utilisateur.
- Ajout d'une variable d'environnement pour limiter la taille des exports d'évaluations.
- Harmonisation du wording "Opcos" en "Opérateur de compétences".
- Ajout d'une migration de données pour rattacher les Parcours aux Opcos.
- Ajout d'une table de liaison entre Opco et parcours type.
- Ajout de la possibilité d'ajouter ou de retirer un parcours type depuis le formulaire d'un opco.
- Seuls les super admin peuvent ajouter un parcours type à un opcos.
- Ajout d'un model opco_parcours_type.
- Affichage de la liste des parcours types associés à une opco.
- Correction du titre de la sidebar :responsable_de_suivi.
- Suppression de l'ancien menu mobile.
- Suppression du code de la modal mise en garde et de ses traductions.
- Passage de la modal acceptation des CGU en DSFR.
- Suppression du JS et du fichier scss associés à l'ancienne modal.
- Suppression des imports de modals dans le fichier bootstrap_minimal.scss.
- Correction du bouton de validation de la modal fusion.
- Correction de la soumission du formulaire de fusion des bénéficiaires.
- Correction du background de la modal.
- Correction du hover du bouton close de la modal confirmation création structure.
- Affichage du nom de la structure et de son adresse dans l'alerte d'invitation à une structure.
- Changement du wording des alertes invitations.
- Correction de la taille des boutons.
- Correction du composant BoutonDSF.
- Correction des boutons annulé sur la partie active admin.
- Correction du bouton menu action.
- Correction des liens des restitutions eva pro.
- Correction des url des restitutions eva pro.
- Correction du double soulignement du lien de l'email dans la recherche de structure dans l'onboarding.
- Correction des marges entre le Header/Contenu et Contenu/footer sur l'ensemble des pages.
- Correction de la version petit écran.
- Correction de la version pdf.
- Correction du linter.
- Ajout de la suppression dans le file input.
- Ajout de la suppression d'une image à son ajout dans le form.
- Ajout de styles et de classes pour le logo dans le header EVA.
- Gère l'état actif pour les menus déroulants.
- Améliore le style des boutons dans l'interface admin.
- Corrige les états des boutons tertiaires sur la page d'inscription.
- Corrige une faute de frappe dans le titre de l'offre de services.
- Corrige les ouvertures de modales.
- Corrige les boutons de la modale.
- Corrige le linter.
- Corrige le comportement des éléments dans le bilan Evapro.
- Corrige le style des boutons dans l'interface admin.
- Corrige les états des boutons tertiaires sur la page d'inscription.
- Corrige une faute de frappe dans le titre de l'offre de services.
- Corrige les ouvertures de modales.
- Corrige les boutons de la modale.
- Corrige le linter.
- Corrige le comportement des éléments dans le bilan Evapro.
