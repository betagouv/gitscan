## Changelog : anssi-recommandations-cyber (30 derniers jours, au 9 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment concernant l'affichage et la gestion des sources, ainsi qu'un nouveau système d'avis utilisateur. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la fluidité de l'application. Des mises à jour de sécurité ont été appliquées pour protéger l'application contre les vulnérabilités connues.

### Évolutions fonctionnelles
- Ajout d'un nouveau formulaire pour recueillir les avis des utilisateurs sur la pertinence et l'exactitude des réponses. Les utilisateurs peuvent désormais soumettre leurs commentaires et évaluer la qualité des informations fournies. [#bedc6ce](https://github.com/betagouv/anssi-recommandations-cyber/commit/bedc6ce)
- Amélioration de l'affichage des sources :
    - Les sources sont maintenant affichées sur toute la largeur de la page. [#992d102](https://github.com/betagouv/anssi-recommandations-cyber/commit/992d102)
    - Possibilité de faire défiler horizontalement les sources via des boutons "suivant" et "précédent". [#80284a2](https://github.com/betagouv/anssi-recommandations-cyber/commit/80284a2)
    - Affichage d'une image générique si le document téléchargé n'est pas un PDF. [#765b055](https://github.com/betagouv/anssi-recommandations-cyber/commit/765b055)
    - Affichage des pages PDF dans un carrousel. [#31c9674](https://github.com/betagouv/anssi-recommandations-cyber/commit/31c9674)
- La page se scrolle automatiquement vers le dernier message de l'utilisateur. [#b449e67](https://github.com/betagouv/anssi-recommandations-cyber/commit/b449e67)
- Les sources sont chargées par défaut. [#33114de](https://github.com/betagouv/anssi-recommandations-cyber/commit/33114de)

### Évolutions techniques
- Modification de l'API pour prendre en compte un nouveau modèle basé sur la pertinence des sources. [#4bb2f94](https://github.com/betagouv/anssi-recommandations-cyber/commit/4bb2f94) et [#805cfd3](https://github.com/betagouv/anssi-recommandations-cyber/commit/805cfd3)
- Ajout de la gestion des raisons pour lesquelles les sources ne sont pas adaptées. [#8aded7d](https://github.com/betagouv/anssi-recommandations-cyber/commit/8aded7d) et [#081308f](https://github.com/betagouv/anssi-recommandations-cyber/commit/081308f)
- Mise en place d'un feature flag pour activer le nouveau formulaire d'avis utilisateur. [#110a145](https://github.com/betagouv/anssi-recommandations-cyber/commit/110a145)
- Refactorisation des routes de l'API conversation. [#8b538c9](https://github.com/betagouv/anssi-recommandations-cyber/commit/8b538c9)
- Utilisation du store `storeAvisUtilisateurBis` pour gérer le formulaire d'avis utilisateur. [#49385a7](https://github.com/betagouv/anssi-recommandations-cyber/commit/49385a7)

### Autres changements
- Ajout d'une documentation sur les interactions entre MQC et Albert. [#2b33f87](https://github.com/betagouv/anssi-recommandations-cyber/commit/2b33f87)
- Corrections de bugs mineurs et améliorations de la qualité du code. [#aa423e4](https://github.com/betagouv/anssi-recommandations-cyber/commit/aa423e4) et [#faca60e](https://github.com/betagouv/anssi-recommandations-cyber/commit/faca60e)
- Mise à jour des dépendances de sécurité : dompurify, svelte, vite, starlette et cryptography. [#47b3579](https://github.com/betagouv/anssi-recommandations-cyber/commit/47b3579), [#8d07820](https://github.com/betagouv/anssi-recommandations-cyber/commit/8d07820), [#bdaa481](https://github.com/betagouv/anssi-recommandations-cyber/commit/bdaa481), [#f7a328b](https://github.com/betagouv/anssi-recommandations-cyber/commit/f7a328b), [#72324d3](https://github.com/betagouv/anssi-recommandations-cyber/commit/72324d3)
- Épingle des versions des dépendances des GitHub Actions pour assurer la reproductibilité des builds. [#3b6e5d2](https://github.com/betagouv/anssi-recommandations-cyber/commit/3b6e5d2)
