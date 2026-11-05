## Changelog : conversations (30 derniers jours, au 04/11/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la sécurisation de la plateforme via la correction de nombreuses vulnérabilités (CVE) et le durcissement des paramètres de sécurité. L'expérience utilisateur a été fluidifiée, notamment par une meilleure gestion des interruptions de réponses et des rechargements de page, tandis que l'observabilité du système a été renforcée pour faciliter le suivi des performances des modèles d'IA.

### Évolutions fonctionnelles
- **Gestion des réponses et de l'IA** : ajout d'une limite de jetons (tokens) par message et amélioration de la continuité des conversations (affichage des appels d'outils et des réponses interrompues après un rechargement de page).
- **Expérience utilisateur (UX)** : 
    - Amélioration de la gestion des mises à jour : incitation au rechargement de la page lors d'un nouveau déploiement pour éviter l'usage de versions obsolètes.
    - Meilleure gestion des erreurs : affichage d'une page de rechargement au lieu d'une page blanche en cas d'erreur.
    - Retours visuels : nouveaux messages de statut lors du traitement des fichiers et ajustements de l'interface (module d'impact carbone, alertes de trafic).
- **Gestion documentaire** : amélioration de la conservation des fichiers originaux attachés aux conversations.

### Évolutions techniques
- **Sécurité** : 
    - Correction massive de vulnérabilités (CVE) via la mise à jour de dépendances critiques (pypdf, authlib, undici, zod, djangorestframework, brotli, certifi, pillow, etc.).
    - Durcissement des paramètres de sécurité Django.
- **Observabilité et monitoring** : 
    - Mise en place de métriques Prometheus pour mesurer les requêtes de modèles, les flux de chat et les appels sortants.
    - Ajout de moniteurs (ServiceMonitor/PodMonitor) pour Helm et configuration du taux d'échantillonnage des traces Sentry.
- **Infrastructure et CI/CD** : 
    - Optimisation de l'environnement Docker (passage à mailcatcher, restriction des ports de développement au localhost).
    - Amélioration de la CI avec une gestion optimisée du cache Playwright.
    - Gestion du fichier `robots.txt` via Helm.
- **Backend et Performance** : 
    - Optimisation de la gestion des tâches asynchrones (timeouts Redis/Celery et gestion du stockage des documents parsés).
    - Nettoyage des données (suppression des caractères NUL dans les conversations).
- **Compatibilité** : amélioration du support des navigateurs plus anciens.

### Autres changements
- **Documentation** : ajout des politiques d'utilisation de l'IA, des procédures de déploiement et de la politique de contribution (Pull Requests).
- **Internationalisation** : mises à jour régulières des chaînes de traduction.
