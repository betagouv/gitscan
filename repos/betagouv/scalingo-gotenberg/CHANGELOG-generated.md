## Changelog : scalingo-gotenberg (30 derniers jours, au 31 août 2026)

### Résumé
Lancement initial du projet permettant le déploiement de Gotenberg sur la plateforme Scalingo. Cette première version établit les bases de l'infrastructure, stabilise l'environnement d'exécution et sécurise les accès réseau.

### Évolutions fonctionnelles
- Retrait du moteur LibreOffice des capacités de conversion disponibles.

### Évolutions techniques
- Initialisation de l'architecture et de la structure du projet.
- Sécurisation du service par une restriction de l'écoute au réseau privé uniquement.
- Correction des chemins d'accès système pour Supervisor et Chromium.
- Optimisation de la gestion des variables d'environnement et du port de démarrage.
- Désactivation des métriques Prometheus.

### Autres changements
- Ajout de la licence Apache-2.0.
- Ajout d'un bouton de déploiement pour faciliter l'installation sur Scalingo.
- Configuration de la branche principale du dépôt.
