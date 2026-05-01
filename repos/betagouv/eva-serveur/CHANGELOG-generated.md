## Changelog : eva-serveur (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment une migration vers le Design System Français (DSFR) pour une interface plus moderne et accessible. Des corrections de bugs et des optimisations ont également été apportées, ainsi que des évolutions concernant la gestion des OPCO et des invitations. Des refactorings importants ont été réalisés pour améliorer la structure du code et la gestion des évaluations.

### Évolutions fonctionnelles
- Les tableaux d'évaluation sont désormais affichés en utilisant le DSFR, améliorant l'accessibilité et l'apparence visuelle.
- Les actualités ont été corrigées pour une meilleure intégration et un affichage correct.
- La page "Ma structure" et la page "Mon compte" ont été améliorées sur mobile.
- Les utilisateurs OPCO peuvent désormais accéder à un dashboard avec des statistiques Metabase.
- Une page dédiée a été ajoutée pour les invitations invalides.
- La gestion des invitations a été améliorée, avec des alertes plus claires et la prise en compte des structures déjà existantes.
- Les structures administratives peuvent désormais inviter des utilisateurs.
- Les parcours d'invitation ont été améliorés avec des informations plus claires et un accès au tableau de bord.
- Possibilité de consulter les explications de comparaison des évaluations littératie et numératie.
- Ajout d'une gestion des usages et des OPCO pour les structures administratives.
- Amélioration de l'affichage des campagnes dans le dashboard Eva Pro.
- Correction de la validation du formulaire de fusion des bénéficiaires.

### Évolutions techniques
- Migration progressive de l'interface utilisateur vers le Design System Français (DSFR), remplaçant les composants Bootstrap.
- Refactoring important du code lié à la gestion des évaluations, avec introduction de nouvelles classes (`DiagnosticPro`, `PassationBeneficiaire`, `ImpactsPresenter`, etc.) pour une meilleure organisation et maintenabilité.
- Suppression de code obsolète (progress bars Bootstrap, modals Bootstrap).
- Mise à jour des dépendances Ruby et Nodejs.
- Amélioration de la sécurité : correction d'une faille d'injection SQL et mise à jour de TarteauCitronJS.
- Optimisation des performances : correction d'un N+1 sur la page des actualités.
- Configuration de Plausible pour le suivi des liens sortants.
- Utilisation de geo.api.gouv.fr pour la géolocalisation des structures.
- Amélioration de la CI avec mise en cache de libvips.

### Autres changements
- Correction de diverses erreurs de style et de typographie.
- Suppression de références à des images et des textes obsolètes.
- Ajout de tests unitaires pour valider les nouvelles fonctionnalités et les corrections de bugs.
- Harmonisation du wording "Opcos" en "Opérateur de compétences".
- Mise à jour de la documentation.
- Suppression du recaptcha.
- Ajout de la police Marianne.
- Correction de l'affichage des PDF.
- Correction de la redirection pour les comptes ProConnect sans structure.
- Ajout d'une validation sur l'extension des fichiers audio.
- Correction de bugs mineurs sur l'interface utilisateur.
- Suppression des utilities Bootstrap.
- Correction des classes Bootstrap non converties en DSFR.
- Amélioration du cache de la CI.
- Ajout de la gestion du code commune.
- Ajout d'un validateur blob d’ActiveStorage pour valider le type audio des transcriptions.
- Correction de l'erreur 500 sur la page index Questionnaires.
- Amélioration de la gestion des erreurs.
- Suppression de l'import des modals dans le fichier bootstrap_minimal.scss.
- Correction du visuel des actualités.
- Correction du hover du breadcrumb.
- Correction de la modale d'invitation.
- Correction de la page aide.
- Correction de la page d'édition de ma structure sur mobile.
- Correction de la page d'accueil sur mobile.
- Correction de la page détail d'un bénéficiaire sur mobile.
- Correction de la page structure en mobile.
- Correction de la page mon compte sur mobile.
- Correction du padding des filtres.
- Correction des marges entre le Header/Contenu et Contenu/footer.
- Correction de l'affichage des boutons.
- Correction de la position des boutons de demo.
- Correction du background de la modal.
- Correction du bouton de validation de la modal fusion.
- Correction du padding left des radio button d'activeadmin.
- Correction du padding inutile dans les filtres.
- Correction de l'intégration des actualités.
- Correction de l'ancien padding/margin des classes bootstrap.
- Correction de la classe mx-auto.
- Correction de l'erreur sur le bouton menu des actualités.
- Ajout d'un test pour vérifier le bouton menu des actualités.
- Correction du tableau Evaluation eva.
- Suppression du numero de Gaelle.
- Ajout de padding sur la version mobile du tableau des evaluations eva.
- Ajout de styles pour l'impression et ajustement de la génération de PDF.
- Ajout du logo evapro dans la démonstration.
- Ajout de la fonctionnalité d'invitation pour les structures administratives.
- Correction de la redirection pour les comptes ProConnect sans structure.
- Suppression du padding left sur tous les commentaires dans les pages détails d'activeadmin.
- Le contenu est maintenant dans un container de max 1200px comme le DSFR.
- Correction de la modal du tableau de bord sur mobile.
- Correction du détail d'une actualité sur mobile.
- Correction de l'interface de la page actualités sur mobile.
- Correction de la modale d'invitation sur mobile.
- Correction du breadcrumb sur mobile.
- Correction de la page mon compte sur mobile.
- Correction du rendu du mobile pour la page aide.
- Correction de l'interface de la page actualités sur mobile.
- Correction de la modale d'invitation sur mobile.
- Correction du breadcrumb sur mobile.
- Correction de la page détail d'un bénéficiaire sur mobile.
- Correction de la page structure en mobile.
- Correction de la page Ma structure.
- Correction de la page mon compte sur mobile.
- Correction de l'interface de la page actualités sur mobile.
- Correction de la modale d'invitation sur mobile.
- Correction du breadcrumb sur mobile.
- Correction de la page détail d'un bénéficiaire sur mobile.
- Correction de la page structure en mobile.
