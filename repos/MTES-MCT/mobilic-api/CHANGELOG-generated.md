## Changelog : mobilic-api (30 derniers jours, au 03/08/2026)

### Résumé
Ce mois-ci, l'API a franchi des étapes importantes dans la gestion du cycle de vie des employés avec l'introduction des demandes de détachement et des processus de contestation. La fiabilité des rapports d'activité (exports PDF et Excel) a été considérablement renforcée, tandis que la stabilité technique a été améliorée, notamment sur l'intégration des webinaires et les performances de la base de données.

### Évolutions fonctionnelles
- **Gestion des employés et détachements** : Ajout de la possibilité de soumettre des demandes de détachement ([#731](https://github.com/MTES-MCT/mobilic-api/pull/731)) et de contester des décisions ([#722](https://github.com/MTES-MCT/mobilic-api/pull/722)). Les emails de notification liés aux détachements ont également été améliorés.
- **Exports et rapports (PDF/XLS)** : Amélioration de la précision des données exportées, incluant une meilleure gestion des fuseaux horaires, l'ajout des temps de pause et une clarification des motifs de litige pour éviter les doublons.
- **Mode impersonation (simulation d'utilisateur)** : Extension des capacités de simulation pour permettre aux administrateurs de créer des missions et de tracer les actions dans les exports ([#732](https://github.com/MTES-MCT/mobilic-api/pull/732), [#749](https://github.com/MTES-MCT/mobilic-api/pull/749)).

### Évolutions techniques
- **Performance et base de données** : Optimisation des performances via l'ajout et la suppression d'index SQL ([#740](https://github.com/MTES-MCT/mobilic-api/pull/740)) et amélioration de la rapidité du tableau de bord.
- **Infrastructure et CI/CD** : Mise en place de "Review Apps" sur Scalingo pour permettre le test isolé de nouvelles fonctionnalités ([#737](https://github.com/MTES-MCT/mobilic-api/pull/737)).
- **Fiabilité et Observabilité** : Résolution de problèmes de délais d'attente (timeouts) sur l'intégration Livestorm et réduction du bruit d'alertes dans Sentry pour une meilleure surveillance ([#724](https://github.com/MTES-MCT/mobilic-api/pull/724)).
- **Sécurité** : Renforcement des contrôles d'accès pour les calculs de régulation administrative ([#741](https://github.com/MTES-MCT/mobilic-api/pull/741)).

### Autres changements
- **Maintenance** : Nettoyage et fusion des branches de migration de la base de données.
- **Tests** : Amélioration de la couverture de tests, notamment sur les fonctionnalités de simulation et les webinaires.
