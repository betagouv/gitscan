## Changelog : grist-core (30 derniers jours, au 31 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'accessibilité, notamment pour les utilisateurs de lecteurs d'écran, ainsi que des corrections et des améliorations au processus de configuration initiale. Des avancées ont également été faites concernant la gestion des autorisations OAuth et la création de copies de documents. De nombreuses traductions ont été mises à jour grâce à la contribution de la communauté.

### Évolutions fonctionnelles
- **Accessibilité :** Amélioration du support des lecteurs d'écran dans les vues de grille, permettant une meilleure expérience pour les utilisateurs ayant des besoins spécifiques. [#2230, #2114]
- **Configuration initiale :** Amélioration du flux de configuration initiale, notamment la vérification de la disponibilité du sandbox et la gestion des erreurs. [#2366, #2341, #2340]
- **OAuth :** Implémentation du flux de consentement OAuth et de la gestion des autorisations. [#15d0aa48]
- **Duplication de documents :** Possibilité de créer une copie d'un document lors de sa modification depuis la fenêtre contextuelle de l'assistant. [#69e26019]
- **Formats de date :** Ajout de nouveaux formats de date. [#2347]
- **Raccourcis clavier :** Ajout de raccourcis clavier pour ouvrir les menus de ligne et de colonne dans les vues de grille. [#2230]
- **Sous-domaines :** Réservation du sous-domaine "forum". [#2351]

### Évolutions techniques
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances, notamment `webpack-dev-server`, `ws`, `multiparty`, `axios`, `fast-uri`, et `basic-ftp`.
- **Amélioration de la logique de détection de la locale :** Amélioration de la logique de détection et de repli de la locale. [#0fe0b5d5]
- **Refactoring :** Unification de la gestion des changements d'authentification avec d'autres changements de configuration en attente. [#2189ef24]
- **Tests :** Corrections et améliorations des tests pour QuickSetupAuth et CustomWidgets. [#04ea880f]
- **Action Summarizer :** Clarification de l'affichage des lignes potentiellement supprimables. [#2361]

### Autres changements
- **Traductions :** Mises à jour des traductions en hongrois, italien, portugais, allemand, indonésien, chinois simplifié, basque et portugais brésilien.
- **Documentation :** Mise à jour du fichier README pour couvrir le flux de configuration rapide. [#2366]
- **CLA :** Signature du CLA par plusieurs contributeurs.
- **Mises à jour de version :** Mises à jour de version internes.
