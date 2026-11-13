## Changelog : element-call-ios (30 derniers jours, au 15 octobre 2026)

### Résumé
Cette période a été consacrée à l'amélioration de l'expérience utilisateur lors des appels directs (DM), notamment par l'ajout de retours visuels et sonores plus intuitifs. Les capacités de test ont également été renforcées pour garantir une meilleure stabilité des appels en tête-à-tête.

### Évolutions fonctionnelles
- **Appels en direct (DM) :** Ajout de l'écran de sonnerie pour les appels sortants [#66](https://github.com/tchapgouv/element-call-ios/pull/66).
- **Interface utilisateur :**
    - Ajout d'ondes sonores autour de l'avatar pour signaler visuellement qu'un interlocuteur parle.
    - Optimisation de l'affichage avec l'utilisation de grands avatars (140 pt) et une interface plus épurée (masquage de la vignette de caméra éteinte).
    - Gestion de l'affichage en mode écouteur (écran noir) pour éviter les pressions accidentelles sur l'écran.
    - Amélioration de la visibilité de la durée de l'appel via une couleur de texte principale.
- **Audio :** Intégration des sons de sonnerie, de refus et de fin de délai (timeout) directement dans le flux audio de l'appel.
- **Logique d'appel :** Meilleure gestion de l'identification de l'auteur de la fin d'un appel.

### Évolutions techniques
- **Mises à jour des SDK :** Intégration des versions récentes de Matrix Rust SDK (26.10.15) et Matrix Rust RTC (0.5.0-rc.5), incluant la résolution de correctifs liés au SDK [#67](https://github.com/tchapgouv/element-call-ios/pull/67).
- **Synchronisation :** Amélioration du suivi des statuts d'appel en s'appuyant sur les états du noyau (core).
- **Tests et démonstration :** Enrichissement de l'environnement de test (*example harness*) pour simuler l'intégralité du cycle de vie d'un appel en tête-à-tête (sonnerie, décrochage, refus, expiration).

### Autres changements
- Publication de la version 0.1.0-rc.11.
