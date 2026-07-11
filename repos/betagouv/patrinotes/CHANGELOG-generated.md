## Changelog : patrinotes (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la génération de rapports PDF, notamment la correction de problèmes d'affichage des images et de mise en page.  L'ajout de Sentry permet également une meilleure surveillance et résolution des erreurs. Des corrections de bugs ont été apportées pour améliorer la stabilité de l'application mobile et de l'interface utilisateur.

### Évolutions fonctionnelles
- Amélioration de la génération des rapports PDF : ajout de commentaires et de procédures dans les rapports de visite v1.
- Correction de l'affichage des images dans les PDF : résolution des problèmes de distorsion, de chevauchement et de positionnement.
- Amélioration de la réactivité de l'application mobile : fermeture correcte du modal des actions mobiles après exécution.
- Correction du lien vers la FAQ.
- Ajout de statistiques d'administration : correction d'une clause `WHERE` manquante dans la route des statistiques d'administration.

### Évolutions techniques
- Intégration de Sentry pour la surveillance des erreurs côté frontend et backend.
- Mise en place de `networkfirst` pour la récupération de la configuration de l'environnement.
- Suppression des balises `<unbreakable />` pour améliorer la compatibilité et la mise en page.

### Autres changements
- Correction de typos diverses.
- Préparation des sprints 6 et 7. [#75](https://github.com/betagouv/patrinotes/issues/75)
