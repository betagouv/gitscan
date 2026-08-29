## Changelog : data_pass (30 derniers jours, au 28/08/2026)

### Résumé
Ce mois-ci, data_pass s'enrichit de nouveaux formulaires et cas d'usage (Nexys, Ianord, DINUM) et améliore l'expérience des agents avec un nouveau mode de consultation pour les formulaires d'instruction. La sécurité a été renforcée par la correction de vulnérabilités et une meilleure gestion des accès, tandis que l'infrastructure a été simplifiée.

### Évolutions fonctionnelles
- **Nouveaux formulaires et cas d'usage** : intégration des formulaires Nexys (MGDIS) [#1731], Ianord (cantines lycées/collèges) [#1710] et des produits DINUM [#1677].
- **Amélioration de l'API Particulier** : ajout de nouveaux périmètres (INE [#1722], AEEH et régime pensionnat [#1709]) et harmonisation des intitulés avec Simplifions [#1744].
- **Interface utilisateur** : 
    - Passage des formulaires d'instruction en mode "consultation" (suppression des boutons de modification et du panneau latéral) [#1701].
    - Ajout d'une interface pour visualiser les emails automatisés [#1681].
    - Clarification des libellés (ex: passage de "Nom de naissance" à "Nom de famille" [#1738]).
- **Workflow** : transmission automatique de la convention aux contacts lors de la validation [#1691].
- **Corrections** : résolution d'erreurs de navigation dans les tunnels de formulaires et correction de la proactivité CNOUS [#1716].

### Évolutions techniques
- **Sécurité** : 
    - Correction d'une vulnérabilité d'injection SQL sur le tri du tableau de bord d'instruction [#1729].
    - Mise à jour de Rails pour corriger une faille de sécurité (CVE-2026-66066) [#1715].
- **Authentification** : rétablissement du scope OAuth HubEE spécifique à DataPass [#1725].
- **Observabilité** : passage à la production de journaux (logs) au format JSON via logstasher [#1714].
- **Infrastructure** : suppression des configurations d'environnement locales au profit d'une gestion centralisée par Ansible [#1717].

### Autres changements
- **Documentation** : mise à jour des guides concernant la politique de retry des webhooks [#1728] et les cadres juridiques Ianord [#1736].
- **Nettoyage** : renommage de variables internes pour une meilleure cohérence (statut boursier) [#1721].
