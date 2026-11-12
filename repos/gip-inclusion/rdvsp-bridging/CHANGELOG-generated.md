## Changelog : rdvsp-bridging (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois-ci a marqué une étape majeure dans la maturité du projet avec l'ajout de la synchronisation Google Calendar et une refonte de la gestion des rendez-vous pour éviter les doublons lors de l'activation de nouveaux services. La plateforme est devenue nettement plus robuste et sécurisée grâce à l'implémentation de nouveaux mécanismes de surveillance, de protections contre les attaques et d'une automatisation complète des déploiements.

### Évolutions fonctionnelles
- **Intégration Google Calendar** : Ajout de la possibilité de connecter des calendriers Google via OAuth ([#09](https://github.com/gip-inclusion/rdvsp-bridging/pull/9)).
- **Gestion intelligente des rendez-vous** : 
    - Possibilité pour l'administrateur d'ignorer les rendez-vous déjà existants avant une connexion pour éviter de polluer les outils tiers ([#10](https://github.com/gip-inclusion/rdvsp-bridging/pull/10)).
    - Amélioration de l'interface d'administration permettant de visualiser les rendez-vous d'une connexion et de libérer les éléments ignorés.
- **Synchronisation Pipedrive** : 
    - Meilleure gestion des activités supprimées dans Pipedrive.
    - Sécurisation de l'authentification des webhooks Pipedrive via Basic Auth.
- **Extraction de données** : Amélioration de la détection et de l'extraction des liens RDV-SP contenus dans les descriptions de rendez-vous.

### Évolutions techniques
- **Sécurité renforcée** :
    - Mise à jour critique de Ruby, Rails et de diverses dépendances pour corriger des vulnérabilités ([#03](https://github.com/gip-inclusion/rdvsp-bridging/pull/3), [#09](https://github.com/gip-inclusion/rdvsp-bridging/pull/9), [#02](https://github.com/gip-inclusion/rdvsp-bridging/pull/2)).
    - Migration du hachage des mots de passe CalDAV vers SHA-256.
    - Mise en place de limites de débit (rate limiting) sur l'administration et l'authentification CalDAV pour prévenir les attaques par force brute.
- **Fiabilité et Observabilité** :
    - Mise en place de tests de santé automatisés (*smoke tests*) après chaque déploiement ([#14](https://github.com/gip-inclusion/rdvsp-bridging/pull/14)).
    - Nouveau système d'alerting pour surveiller les échecs d'importation RDV-SP et l'état de connexion des comptes.
    - Optimisation des migrations de base de données avec des timeouts pour éviter les blocages en production.
- **Infrastructure et Déploiement** :
    - Migration du service vers le domaine `pont-rdv.inclusion.gouv.fr` ([#13](https://github.com/gip-inclusion/rdvsp-bridging/pull/13)).
    - Automatisation complète du cycle de déploiement sur Scaleway via GitHub Actions ([#01](https://github.com/gip-inclusion/rdvsp-bridging/pull/1)).
    - Configuration de la confiance des proxys Scaleway pour assurer la remontée correcte des adresses IP ([#11](https://github.com/gip-inclusion/rdvsp-bridging/pull/11)).
- **Cœur du système** : Implémentation du serveur CalDAV, de la gestion des jetons de synchronisation (*sync tokens*) et de la synchronisation bidirectionnelle des disponibilités.

### Autres changements
- Renommage officiel du projet en `rdvsp-bridging`.
- Ajout des traductions françaises pour le framework Rails.
- Mise à jour de la documentation technique et du journal de décisions (decision log).
