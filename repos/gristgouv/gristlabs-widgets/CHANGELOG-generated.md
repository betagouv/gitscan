## Changelog : gristlabs-widgets (30 derniers jours, au 19 juin 2026)

### Résumé
Cette mise à jour se concentre sur l'amélioration de la robustesse et de la clarté de l'affichage des widgets, notamment en gérant mieux les erreurs et en simplifiant la présentation des titres et labels. Une préparation pour la publication de la version 0.0.7 a également été effectuée.

### Évolutions fonctionnelles
- Les erreurs et les messages d'inspection sont désormais affichés en texte brut, améliorant la lisibilité et évitant les problèmes d'interprétation du HTML.  [#225](https://github.com/gristlabs/gristlabs-widgets/issues/225)
- Les labels des widgets sont maintenant rendus en texte brut au lieu de HTML, pour une présentation plus simple et prévisible. [#221](https://github.com/gristlabs/gristlabs-widgets/issues/221)
- L'affichage du message d'erreur et du message d'exoplanète a été corrigé pour afficher du texte. [#227](https://github.com/gristlabs/gristlabs-widgets/issues/227)
- Amélioration de la sanitisation des titres pour éviter des problèmes d'affichage. [#223](https://github.com/gristlabs/gristlabs-widgets/issues/223)

### Évolutions techniques
- Les tests ont été mis à jour pour fonctionner avec la dernière image de Grist. [#219](https://github.com/gristlabs/gristlabs-widgets/issues/219)
- Toutes les dépendances ont été déplacées vers `devDependencies`, réduisant la taille du bundle final. [#218](https://github.com/gristlabs/gristlabs-widgets/issues/218)

### Autres changements
- Préparation de la publication de la version 0.0.7.
