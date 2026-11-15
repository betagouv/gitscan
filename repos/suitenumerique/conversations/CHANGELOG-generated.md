## Changelog : conversations (30 derniers jours, au 14 novembre 2026)

### Résumé
Ce mois-ci, le projet a considérablement enrichi ses capacités d'analyse de données en permettant l'utilisation de calculatrices précises et la génération de graphiques à partir de fichiers tableurs (CSV, XLSX). L'expérience de discussion a été fluidifiée, notamment pour mieux gérer les réponses longues ou les interruptions de l'utilisateur. Parallèlement, un effort majeur a été porté sur la sécurité du système et la mise en place d'outils de surveillance pour garantir la stabilité du service.

### Évolutions fonctionnelles
- **Analyse de données et calculs** :
    - Ajout d'un outil de calcul pour garantir des résultats arithmétiques exacts.
    - Capacité d'analyser des pièces jointes CSV et XLSX via un outil de requête structurée.
    - Génération automatique de graphiques à partir des résultats de requêtes sur tableurs.
    - Ajout d'un indicateur visuel ("calcul en cours") lors de l'utilisation de la calculatrice.
- **Expérience utilisateur (UX)** :
    - Amélioration de la gestion des réponses : affichage clair des interruptions, meilleure gestion des rechargements de page et maintien de l'historique lors des interruptions.
    - Optimisation de l'interface : masquage des actions de réponse pendant la génération et correction de l'alignement de certains menus.
    - Amélioration de la compatibilité avec les navigateurs plus anciens.
    - Conservation du fichier original lors de l'ajout de documents à une conversation.

### Évolutions techniques
- **Sécurité** :
    - Campagne massive de mise à jour des dépendances pour corriger plusieurs vulnérabilités (CVE) critiques.
    - Renforcement des paramètres de sécurité de Django.
    - Configuration de la gestion des rôles OIDC.
- **Observabilité et Monitoring** :
    - Mise en place de métriques Prometheus pour suivre les requêtes de modèles, les flux de chat et les appels sortants.
    - Implémentation de logs structurés au format JSON pour la production.
    - Configuration de la télémétrie Sentry et des outils de monitoring Helm (ServiceMonitor/PodMonitor).
- **Architecture et Performance** :
    - Refactoring important du service "agent" pour séparer la gestion des tours de parole, de la persistance et du calcul de jetons (tokens).
    - Ajout de limites de jetons de sortie par message pour contrôler la consommation.
    - Ajout de timeouts pour les clients Redis et Celery afin d'améliorer la résilience.
- **Infrastructure et CI/CD** :
    - Optimisation du cache Playwright dans les pipelines de tests.
    - Mise à jour de l'infrastructure Helm et remplacement de Maildev par Mailcatcher.

### Autres changements
- **Internationalisation** : Mise à jour de plusieurs chaînes de caractères traduites.
- **Configuration** : Ajout de la gestion d'un fichier `robots.txt` personnalisé.
