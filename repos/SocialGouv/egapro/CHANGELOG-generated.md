## Changelog : egapro (30 derniers jours, au 2026-07-30)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment des corrections de bugs concernant l'affichage des données, la navigation et la soumission des déclarations. Des améliorations techniques ont été apportées pour faciliter le déploiement, la gestion des environnements de test et l'accessibilité. L'ajout du numéro de version dans le footer permet une meilleure identification de la version utilisée.

### Évolutions fonctionnelles
- Ajout du numéro de version dans le footer de l'application. [#4047](https://github.com/SocialGouv/egapro/issues/4047)
- Correction de l'alignement de l'alerte "Prochaines étapes" avec l'indicateur G. [#4049](https://github.com/SocialGouv/egapro/issues/4049)
- Correction du dénominateur des proportions variable H/F dans la déclaration. [#4048](https://github.com/SocialGouv/egapro/issues/4048)
- Amélioration de la documentation des écarts dans l'API publique, en les présentant comme des ratios avec la bonne convention de signe. [#4041](https://github.com/SocialGouv/egapro/issues/4041)
- Correction de l'affichage des écarts, désormais tronqués à deux décimales. [#4039](https://github.com/SocialGouv/egapro/issues/4039)
- Rendre le seuil de 5% symétrique. [#4040](https://github.com/SocialGouv/egapro/issues/4040)
- Masquage de la section CSE lorsque aucun avis n'est attendu. [#4032](https://github.com/SocialGouv/egapro/issues/4032)
- Correction du parcours "justification des écarts" sans CSE. [#4027](https://github.com/SocialGouv/egapro/issues/4027)
- Correction des accordéons inutilisables après suppression puis ré-import. [#4025](https://github.com/SocialGouv/egapro/issues/4025)
- Correction de la deadline de la déclaration 2 en phase 2 et ré-soumission de la deuxième déclaration depuis l'état "en attente de choix". [#4003](https://github.com/SocialGouv/egapro/issues/4003)
- Correction de l'affichage du bandeau entreprise et du libellé d'étape de la démarche "Représentation". [#4024](https://github.com/SocialGouv/egapro/issues/4024)
- Correction des bordures invisibles des cases à cocher et des radios sous Firefox. [#4026](https://github.com/SocialGouv/egapro/issues/4026)
- Prévention des téléchargements multiples de PDF en cas de clics répétés. [#4019](https://github.com/SocialGouv/egapro/issues/4019)
- Correction de l'affichage du panneau latéral en fonction de la taille et du flag CSE. [#4000](https://github.com/SocialGouv/egapro/issues/4000)
- Correction de la position des caractères combinants dans les polices embarquées des PDF. [#4018](https://github.com/SocialGouv/egapro/issues/4018)
- Blocage de la soumission du formulaire si les champs de rémunération sont manquants pour un effectif non nul. [#4002](https://github.com/SocialGouv/egapro/issues/4002)
- Ajout des champs d'écart dans l'API SUIT pour l'export. [#3992](https://github.com/SocialGouv/egapro/issues/3992)
- Affichage de la source des catégories d'emplois en libellé lisible dans le PDF. [#4016](https://github.com/SocialGouv/egapro/issues/4016)
- Message d'erreur CSE plus explicite en français dans le bandeau informations manquantes. [#3997](https://github.com/SocialGouv/egapro/issues/3997)
- Ajout du bouton "Je donne mon avis" en fin de parcours. [#3966](https://github.com/SocialGouv/egapro/issues/3966)
- Implémentation du versioning des CGU. [#2626](https://github.com/SocialGouv/egapro/issues/2626)
- Ajout d'un texte explicatif du bouton plus info. [#2624](https://github.com/SocialGouv/egapro/issues/2624)
- Intégration des contenus des emails de confirmation et leurs règles d'envoi. [#3849](https://github.com/SocialGouv/egapro/issues/3849)

### Évolutions techniques
- La promotion bake la version dans l'image (app_version).
- Les environnements de test persistants déploient une image versionnée.
- Correction des permissions OIDC manquantes sur le workflow de promotion des environnements de test. [#3908](https://github.com/SocialGouv/egapro/issues/3908)
- Correction de l'échec de la création du tag sur la protection de branche. [#3906](https://github.com/SocialGouv/egapro/issues/3906)
- Création d'environnements de test persistants (RGAA / perf) déployables uniquement depuis des releases. [#3904](https://github.com/SocialGouv/egapro/issues/3904)
- Refonte du moteur d'étapes FSM avec un verrou compilateur. [#3979](https://github.com/SocialGouv/egapro/issues/3979)
- Dérivation du vocabulaire de statut admin de DECLARATION_FSM_STATUSES. [#3983](https://github.com/SocialGouv/egapro/issues/3983)
- Migration des builds d'images de buildkit-service vers buildkit-operator. [#3844](https://github.com/SocialGouv/egapro/issues/3844)
- Refonte multi-pages du template PDF (maquettes). [#3973](https://github.com/SocialGouv/egapro/issues/3973)

### Autres changements
- Correction du changelog IA exhaustif. [#4046](https://github.com/SocialGouv/egapro/issues/4046)
- Correction de l'import GIP qui attend la fin du rollout. [#4058](https://github.com/SocialGouv/egapro/issues/4058)
- Documentation du workflow Figma sur le serveur MCP officiel. [#3881](https://github.com/SocialGouv/egapro/issues/3881)
- Mise à jour des règles d'autorité du moteur d'étapes (FSM). [#3982](https://github.com/SocialGouv/egapro/issues/3982)
- Ajout de tests unitaires et E2E pour le parcours de déclaration. [#3988](https://github.com/SocialGouv/egapro/issues/3988)
- Amélioration de la nomenclature des cas de tests. [#4006](https://github.com/SocialGouv/egapro/issues/4006)
- Changement du CLI pour la génération du changelog IA. [#4009](https://github.com/SocialGouv/egapro/issues/4009)
- Ajout de buckets pour la plage d'effectif 100-149 dans le mock GIP-MDS. [#3991](https://github.com/SocialGouv/egapro/issues/3991)
- Suppression du code NAF et restauration du libellé de l'effectif dans le bandeau CompanyBanner. [#4013](https://github.com/SocialGouv/egapro/issues/4013)
- Ajout de l'implémentation de l'accessibilité avec ultra11y. [#3887](https://github.com/SocialGouv/egapro/issues/3887)
- Ajout de la purge des données des déclarations. [#3828](https://github.com/SocialGouv/egapro/issues/3828)
- Mise en place de la demande du niveau eidas2 (2FA) sur ProConnect. [#3829](https://github.com/SocialGouv/egapro/issues/3829)
