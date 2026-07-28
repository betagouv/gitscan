## Changelog : egapro (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment dans la déclaration de rémunération et la gestion des PDF exportés. Des corrections ont été apportées pour améliorer la clarté des informations et la conformité aux règles métiers. Des optimisations techniques ont également été réalisées pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- Le bouton d'export est de nouveau disponible dans l'étape 5 du parcours de déclaration de rémunération [#3732](https://github.com/SocialGouv/egapro/issues/3732).
- Un bouton "Je donne mon avis" a été ajouté à la fin du parcours de déclaration [#3966](https://github.com/SocialGouv/egapro/issues/3966).
- La source des catégories d'emplois est maintenant affichée de manière lisible dans les PDF exportés [#4016](https://github.com/SocialGouv/egapro/issues/4016).
- Le message d'erreur concernant le CSE est maintenant explicite en français dans la section "informations manquantes" [#3997](https://github.com/SocialGouv/egapro/issues/3997).
- L'effectif et le libellé de l'effectif sont restaurés dans le CompanyBanner, le code NAF ayant été retiré [#4013](https://github.com/SocialGouv/egapro/issues/4013).
- Amélioration de l'affichage de la proportion de bénéficiaires dans l'étape 6 et dans le PDF [#3869](https://github.com/SocialGouv/egapro/issues/3869).
- Implémentation de règles pour l'envoi de notifications par email et contenu des emails [#3857](https://github.com/SocialGouv/egapro/issues/3857) et [#3849](https://github.com/SocialGouv/egapro/issues/3849).
- Ajout de la prise en charge des données GIP pour l'affichage, le parcours et l'export SUIT [#3929](https://github.com/SocialGouv/egapro/issues/3929).

### Évolutions techniques
- Refactor du moteur d'étapes FSM (Finite State Machine) pour améliorer la compilation et la gestion des états [#3979](https://github.com/SocialGouv/egapro/issues/3979).
- Dérivation du vocabulaire de statut admin à partir de `DECLARATION_FSM_STATUSES` pour une meilleure cohérence [#3983](https://github.com/SocialGouv/egapro/issues/3983).
- Amélioration de la conformité des tests E2E avec les spécifications et élagage des tests redondants [#3988](https://github.com/SocialGouv/egapro/issues/3988) et [#3987](https://github.com/SocialGouv/egapro/issues/3987).
- Mise en place d'un canal de publication "prerelease alpha" avec déclenchement automatique [#3858](https://github.com/SocialGouv/egapro/issues/3858).
- Amélioration de la gestion des permissions OIDC pour les workflows CI/CD [#3908](https://github.com/SocialGouv/egapro/issues/3908).
- Correction d'un problème de création de tag GPG lors de la publication [#3906](https://github.com/SocialGouv/egapro/issues/3906).
- Mise en place d'environnements de test persistants pour les tests RGAA et de performance [#3904](https://github.com/SocialGouv/egapro/issues/3904).
- Correction d'un problème de protection de branche lors de la publication sur le canal "prerelease alpha" [#3905](https://github.com/SocialGouv/egapro/issues/3905).
- Intégration d'un système d'accessibilité (ultra11y) [#3887](https://github.com/SocialGouv/egapro/issues/3887).
- Migration des builds d'images vers buildkit-operator [#3844](https://github.com/SocialGouv/egapro/issues/3844).
- Ajout d'un gate de fidélité visuelle avec design-validator (Figma ↔ rendu) [#3749](https://github.com/SocialGouv/egapro/issues/3749).

### Autres changements
- Documentation mise à jour concernant la nomenclature des cas de test [#4006](https://github.com/SocialGouv/egapro/issues/4006) et la discipline de fidélité Figma [#3961](https://github.com/SocialGouv/egapro/issues/3961).
- Correction du seed des données Matomo en local [#3787](https://github.com/SocialGouv/egapro/issues/3787).
- Correction du workflow de release pour utiliser le CLI au lieu de claude-code-action [#4009](https://github.com/SocialGouv/egapro/issues/4009).
- Ajout d'un bucket "medium-150" pour couvrir la tranche d'effectif de 100-149 dans les mocks GIP-MDS [#3991](https://github.com/SocialGouv/egapro/issues/3991).
- Ajout de champs `*_ecart` à la catégorie d'indicateur G dans l'API d'export SUIT [#3993](https://github.com/SocialGouv/egapro/issues/3993).
- Filtrage de `step_change` dans l'historique du statut SUIT et alignement de l'OpenAPI avec le FSM [#3996](https://github.com/SocialGouv/egapro/issues/3996).
- Correction de l'affichage des colonnes Start date et End date dans le board [#3990](https://github.com/SocialGouv/egapro/issues/3990).
- Suppression des tests subsumés par le verrou FSM et la table de décision [#3987](https://github.com/SocialGouv/egapro/issues/3987).
- Correction du contraste des tags "élevé" et des encarts d'avertissement pour l'accessibilité [#3758](https://github.com/SocialGouv/egapro/issues/3758).
- Correction d'un problème de lecture seule après la date limite de modification [#3798](https://github.com/SocialGouv/egapro/issues/3798).
- Refactor de l'unification de l'impersonation et du verrou collaboratif dans LockContext [#3794](https://github.com/SocialGouv/egapro/issues/3794).
- Amélioration du design de la déclaration de rémunération (pages 1-5) [#3935](https://github.com/SocialGouv/egapro/issues/3935).
- Rationalisation de la suite de tests E2E, en se concentrant sur les parcours critiques [#3928](https://github.com/SocialGouv/egapro/issues/3928).
- Correction de l'implémentation du niveau Eidas2 (2FA) sur ProConnect (revert) [#3907](https://github.com/SocialGouv/egapro/issues/3907).
