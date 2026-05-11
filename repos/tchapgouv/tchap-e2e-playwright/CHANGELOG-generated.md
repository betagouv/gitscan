## Changelog : tchap-e2e-playwright (30 derniers jours, au 2026-05-07)

### Résumé
Cette mise à jour apporte des corrections importantes concernant la création de salles et la déconnexion, améliorant ainsi la fiabilité des tests automatisés.  De plus, des ajustements ont été effectués pour garantir la compatibilité avec les dernières versions de Playwright et pour optimiser l'exécution des tests en CI.

### Évolutions fonctionnelles
- Correction d'un problème empêchant la création de salles [#40](https://github.com/tchapgouv/tchap-e2e-playwright/issues/40).
- Correction du test de déconnexion pour une meilleure fiabilité.
- Mise à jour du code de vérification dans les tests pour refléter les changements récents.

### Évolutions techniques
- Mise à jour de Playwright vers la version v1.59.1-noble pour bénéficier des dernières améliorations et corrections [#38](https://github.com/tchapgouv/tchap-e2e-playwright/issues/38).
- Déplacement d'un module dans le dossier `synapse` pour une meilleure organisation du code.
- Ajout d'une nouvelle tentative (`int02`) dans la configuration de la CI pour améliorer la stabilité des exécutions.

### Autres changements
- Aucun changement significatif à signaler.
