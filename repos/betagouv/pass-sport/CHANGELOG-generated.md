## Changelog : pass-sport (30 derniers jours, au 02 novembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration des outils de gestion pour les équipes de support et l'administration (nouveaux processus CNAF, gestion des bénéficiaires AAH), ainsi que sur la modernisation de l'infrastructure technique et de la gestion des flux de données.

### Évolutions fonctionnelles
- **Amélioration des outils de support** : prise en compte des bénéficiaires AAH et amélioration de la gestion des imports de fichiers CSV (support des en-têtes techniques).
- **Nouveaux processus administratifs** : intégration de nouveaux processus liés à la CNAF (AEEH et processus du 10/06/2026). [#644](https://github.com/betagouv/pass-sport/pull/644)
- **Expérience utilisateur** : mise à jour des motifs dans le formulaire de contact [#654](https://github.com/betagouv/pass-sport/pull/654) et amélioration de la gestion des erreurs 404 lors des relances FranceConnect. [#641](https://github.com/betagouv/pass-sport/pull/641)
- **Administration** : mise à disposition d'un tableau de bord accessible via un chemin sécurisé. [#671](https://github.com/betagouv/pass-sport/pull/671)

### Évolutions techniques
- **Gestion des données** : mise en place d'un nouveau pipeline de synchronisation de données avec Grist (Grist-DN). [#670](https://github.com/betagouv/pass-sport/pull/670)
- **Déploiement progressif** : introduction de "feature flags" pour contrôler l'accès aux pages de statistiques et au tableau de bord. [#626](https://github.com/betagouv/pass-sport/pull/626)
- **Infrastructure et DevOps** : 
    - Mise à jour majeure de Next.js et de l'API Crisp. [#678](https://github.com/betagouv/pass-sport/pull/678)
    - Séparation des stacks Docker locales (WAF vs non-WAF).
    - Optimisation de la configuration Nginx et de la gestion du cache.
- **Maintenance et sécurité** : mises à jour de Sentry et des dépendances critiques pour la sécurité du système.

### Autres changements
- **Interface** : ajustements visuels incluant le retrait de certains bandeaux d'information et de notices.
- **Nettoyage** : suppression de tests SQL Python obsolètes et optimisation de la structure des champs de saisie des allocataires.
