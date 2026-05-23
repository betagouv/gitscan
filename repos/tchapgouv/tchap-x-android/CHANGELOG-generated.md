## Changelog : tchap-x-android (30 derniers jours, au 21 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application, notamment un changement de nom de "Tchap X" à "Tchap", la préparation pour les releases avec un script dédié et des corrections de textes. Des ajustements ont également été faits pour faciliter la gestion des environnements de développement et de pré-production. L'interface utilisateur a été mise à jour avec le nouveau logo Tchap et des captures d'écran spécifiques.

### Évolutions fonctionnelles
- Changement de nom de l'application : l'application est désormais nommée "Tchap" au lieu de "Tchap X" [#179](https://github.com/tchapgouv/tchap-x-android/pull/179).
- Ajout du nouveau logo Tchap dans la liste des sessions.
- Mise à jour des captures d'écran de l'application.
- Correction de textes dans l'interface utilisateur.
- Modification de la description de l'onglet "Espace".

### Évolutions techniques
- Mise en place d'un script de génération de release pour Tchap [#179](https://github.com/tchapgouv/tchap-x-android/pull/179).
- Utilisation temporaire du format de version Major/Minor/Patch.
- Renommage des variants de build : `devTchap` et `bTchap` sont maintenant `tchapDev` et `tchapPreprod`.
- Nettoyage des `access_rules` à la création de salons.
- Préparation pour les releases 0.9.0 et 0.10.0.

### Autres changements
- Ajout de previews spécifiques à Tchap.
- Ajout d'un suffixe temporaire "beta".
- Création d'un changelog spécifique pour les modifications Tchap.
