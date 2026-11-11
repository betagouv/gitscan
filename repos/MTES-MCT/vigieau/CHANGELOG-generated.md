## Changelog : vigieau (30 derniers jours, au 2026-11-09)

### Résumé
Cette période a été principalement consacrée au renforcement de la sécurité de la plateforme, notamment par l'intégration d'un système de détection de virus pour les documents. Des efforts importants ont également été fournis pour fiabiliser les données statistiques et corriger des comportements erronés lors du chevauchement de zones géographiques.

### Évolutions fonctionnelles
- **Sécurisation des documents** : Intégration d'un scan antivirus (ClamAV) pour les documents téléchargés et les fichiers existants avant leur publication [#87](https://github.com/MTES-MCT/vigieau/pull/87).
- **Fiabilité des données** : Correction des erreurs de calcul impactant les statistiques de surface départementale et les statistiques d'audience.
- **Gestion des zones** : Résolution des conflits lors du chevauchement de zones géographiques présentant des restrictions équivalentes [#83](https://github.com/MTES-MCT/vigieau/pull/83).
- **Gestion des abonnements** : Rétablissement de la gestion sécurisée des abonnements et correction des liens de confirmation par e-mail [#85](https://github.com/MTES-MCT/vigieau/pull/85).

### Évolutions techniques
- **Sécurité et maintenance** : Mise à jour majeure des dépendances (Node, npm, Nuxt 4) et correction de vulnérabilités critiques, notamment sur la gestion du prototype (`deepmerge`) et le parsing multipart.
- **Stockage et infrastructure** : Optimisation de la gestion des fichiers sur S3 pour garantir la compatibilité avec les environnements OVH et assurer la cohérence entre l'inventaire des documents et les répertoires physiques.
- **Tests et CI/CD** : Renforcement de la chaîne de tests avec l'ajout de vérifications de sécurité, de tests de régression et de validation de la quarantaine antivirus dans la CI.

### Autres changements
- **Accessibilité** : Mise à jour de la déclaration d'accessibilité suite aux derniers audits de conformité [#84](https://github.com/MTES-MCT/vigieau/pull/84).
- **Documentation** : Amélioration de la documentation technique concernant l'exécution des processus antivirus et les services de messagerie (Brevo).
- **Qualité de code** : Finalisation du linting pour l'interface d'administration.
