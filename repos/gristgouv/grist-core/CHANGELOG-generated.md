## Changelog : grist-core (30 derniers jours, au 31 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité, l'expérience utilisateur lors de la configuration initiale, et l'ajout de nouvelles fonctionnalités comme la gestion du consentement OAuth. Des traductions ont également été ajoutées et améliorées pour plusieurs langues.

### Évolutions fonctionnelles
- **Accessibilité:** Amélioration du support des lecteurs d'écran dans les vues de grille, incluant la navigation au clavier pour l'ouverture des menus de ligne et de colonne. [#2230, #2114]
- **Configuration initiale:** Amélioration du flux de configuration rapide (Quick Setup) avec des étiquettes plus claires et une vérification précoce de la sandbox. [#2366, #2341]
- **OAuth:** Implémentation du flux de consentement OAuth et de la gestion des autorisations. [#2363]
- **Formats de date:** Ajout de nouveaux formats de date. [#2037, #2347]
- **Fork de document:** Possibilité de créer une copie (fork) d'un document lorsqu'il est modifié depuis la fenêtre d'assistant.
- **Action Summarizer:** Clarification de l'affichage des lignes potentiellement supprimables. [#2361]

### Évolutions techniques
- **Gestion des locales:** Amélioration de la détection et de la gestion des locales (langues) pour une meilleure internationalisation. [#2313]
- **Mises à jour:** Mise à jour de `webpack-dev-server` (5.2.2 -> 5.2.4) et `ws` (8.20.0 -> 8.20.1) ainsi que `multiparty` (4.2.2 -> 4.3.0). [#2357, #2359, #2355]
- **Tests:** Ajustements de certains tests pour supporter les redémarrages de serveur pendant l'exécution. [#2356]
- **Sous-domaines:** Réservation du sous-domaine "forum". [#2351]

### Autres changements
- **Traductions:** Ajout et amélioration des traductions pour les langues suivantes : Hongrois, Italien, Portugais (Portugal et Brésil), Allemand, Indonésien, Basque.
- **CLA:** Signature du CLA (Contributor License Agreement) par plusieurs contributeurs. [#2363, #2354]
- **Mise à jour de version:** Mise à jour de la version grist-ee.
