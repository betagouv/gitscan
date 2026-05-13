## Changelog : hyyypertool (30 derniers jours, au 12 mai 2026)

### Résumé
Les dernières mises à jour de Hyyypertool se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'un mode sombre, des améliorations de l'interface et des corrections de bugs. Des fonctionnalités importantes ont été ajoutées pour la gestion des modèles de réponses et le filtrage des modérations. Des optimisations techniques et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de l'outil.

### Évolutions fonctionnelles
- Ajout d'un mode sombre pour une meilleure lisibilité et un confort visuel accru.
- Possibilité de filtrer les modérations par statut de décision (acceptées, rejetées, réouvertes) [#1594](https://github.com/proconnect-gouv/hyyypertool/issues/1594).
- Ajout d'une action de suppression pour les modèles de réponses [#1600](https://github.com/proconnect-gouv/hyyypertool/issues/1600).
- Possibilité d'éditer les modèles de réponses directement dans l'application [#1381](https://github.com/proconnect-gouv/hyyypertool/issues/1381).
- Ajout du libellé pour la tranche effectif d'une unité légale [#1520](https://github.com/proconnect-gouv/hyyypertool/issues/1520).
- Suppression du prénom et du nom de famille des emails de rejet pour une meilleure confidentialité [#1576](https://github.com/proconnect-gouv/hyyypertool/issues/1576).
- Améliorations de l'interface utilisateur, notamment pour les modèles de réponses et l'accessibilité.
- Correction d'un bug empêchant l'envoi de l'en-tête `Cache-Control` pour les ressources statiques, améliorant ainsi la performance du cache navigateur [#1603](https://github.com/proconnect-gouv/hyyypertool/issues/1603) et [#1601](https://github.com/proconnect-gouv/hyyypertool/issues/1601).

### Évolutions techniques
- Correction d'un bug dans le seed des modèles de réponses, assurant le chargement correct de tous les templates [#1602](https://github.com/proconnect-gouv/hyyypertool/issues/1602).
- Déplacement de la logique du mode sombre vers un fichier script côté client pour une meilleure organisation.
- Mises à jour de plusieurs dépendances (typescript, preact, hono, drizzle-kit, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.

### Autres changements
- Amélioration de la documentation et des commentaires de code.
- Correction de problèmes mineurs d'interface utilisateur et d'accessibilité.
- Optimisation du code pour une meilleure performance.
