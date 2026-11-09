## Changelog : conversations (30 derniers jours, au 05/11/2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur la fiabilité de l'expérience de chat, notamment pour mieux gérer les interruptions de réponse et les rechargements de page. Un effort majeur a été porté sur la sécurité du système via la correction de nombreuses vulnérabilités et le renforcement des paramètres de l'application. Enfin, de nouveaux outils de surveillance ont été intégrés pour permettre un meilleur suivi technique des performances et de l'utilisation de l'intelligence artificielle.

### Évolutions fonctionnelles
- **Expérience de chat** : Amélioration de la gestion des interruptions (affichage de notices claires) et de la continuité des réponses lors du rechargement de la page.
- **Contrôle des ressources** : Ajout d'une limite de jetons (tokens) de sortie par message.
- **Interface utilisateur** : Amélioration de la clarté des messages lors du traitement des fichiers et ajustements visuels sur le module d'impact carbone.
- **Gestion documentaire** : Les fichiers originaux sont désormais mieux préservés lorsqu'ils sont attachés à une conversation.
- **Compatibilité** : Amélioration du support des navigateurs web plus anciens.

### Évolutions techniques
- **Sécurité** : Mise à jour massive des dépendances pour corriger plusieurs vulnérabilités (CVE) et durcissement des paramètres de sécurité Django.
- **Architecture** : Refactorisation du service "agent" pour mieux séparer la préparation des prompts, la persistance des données et le comptage des jetons.
- **Observabilité** : Implémentation de métriques Prometheus pour mesurer les requêtes de modèles, les flux de chat et les appels sortants, avec intégration de monitoring (ServiceMonitor/PodMonitor).
- **Stabilité et Performance** : 
    - Ajout de timeouts pour les clients Redis et Celery.
    - Optimisation du stockage des documents et du backend de résultats Celery.
    - Amélioration de la gestion des caractères spéciaux (NUL) dans les conversations.
- **Infrastructure et CI/CD** : 
    - Optimisation du cache Playwright dans la CI.
    - Mise à jour de l'environnement Docker (passage à Mailcatcher).

### Autres changements
- **Documentation** : Ajout d'une politique d'utilisation de l'IA et d'une politique de contribution (Pull Requests).
- **Internationalisation** : Mise à jour de plusieurs chaînes de caractères traduites.
- **Configuration** : Possibilité de servir un fichier `robots.txt` personnalisé depuis le frontend.
