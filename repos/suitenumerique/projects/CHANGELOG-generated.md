## Changelog : projects (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations visuelles et de confort d'utilisation, notamment concernant le logo, la favicon et la gestion de la langue. Des corrections de bugs ont également été implémentées pour améliorer la stabilité de l'application, en particulier au niveau de l'affichage de la favicon et du chargement de la langue lors de la connexion. Enfin, la documentation d'auto-hébergement a été mise à jour.

### Évolutions fonctionnelles
- Le logo par défaut et la favicon ont été mis à jour pour utiliser les ressources de l'OSS en fonction du schéma de couleurs.
- La langue par défaut pour les utilisateurs non authentifiés a été corrigée.
- Le chargement de la langue principale est maintenant effectué avant le rendu de l'écran de connexion, évitant ainsi des problèmes d'affichage.

### Évolutions techniques
- Correction d'un problème lié aux rappels de `ResizeObserver` en environnement de développement, évitant ainsi une erreur bénigne.
- La largeur du bouton d'appel à l'action (CTA) sur la page d'accueil a été adaptée à la longueur du texte.

### Autres changements
- Mise à jour de la documentation d'auto-hébergement. [#68ae28d](https://github.com/suitenumerique/projects/commit/68ae28d)
