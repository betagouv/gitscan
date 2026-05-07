## Changelog : docs (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et l'expérience utilisateur, avec des corrections de bugs significatives dans l'interface utilisateur, la gestion des documents et la collaboration. Des optimisations ont été apportées à la gestion du contenu, notamment avec l'introduction d'endpoints dédiés pour le streaming et la mise à jour du contenu, ainsi qu'une refonte de la gestion des threads. Une mise à niveau majeure de la spécification Docspec a également été intégrée.

### Évolutions fonctionnelles
- Ajout d'un lien vers la documentation dans le menu d'aide.
- Intégration de Crisp (outil de chat) dans le menu d'aide.
- Amélioration de l'expérience utilisateur des liens internes (interlinking) avec une nouvelle interface et correction de bugs liés à l'exportation et au focus.
- Possibilité d'ouvrir les liens internes avec le bouton central de la souris ou les touches Ctrl/Cmd.
- Amélioration de la gestion des documents épinglés, désormais triés par date de dernière modification.
- Mise en place d'un endpoint dédié pour le streaming du contenu S3, améliorant les performances.
- Création d'un endpoint dédié pour la mise à jour du contenu des documents.
- Suppression de l'endpoint déprécié pour les descendants de documents.
- Amélioration de la gestion des erreurs 5xx avec une structure d'alerte plus accessible.
- Amélioration de l'accessibilité des étiquettes des résultats de recherche de documents pour les lecteurs d'écran.

### Évolutions techniques
- Mise à niveau de Docspec vers la version 3.0.0, nécessitant des adaptations de l'API de conversion.
- Refonte de la gestion des threads, avec suppression de la pagination.
- Utilisation de Uvicorn pour exécuter l'application Django en environnement de développement.
- Amélioration de la sécurité avec la validation des emojis pour les réactions.
- Amélioration de la sécurité avec la mise à jour de la librairie Axios.
- Amélioration de la sécurité avec la mise à jour de la librairie UUID.
- Amélioration de la sécurité avec la mise à jour de la librairie LXML.
- Amélioration de la sécurité avec la mise à jour de Next.js.
- Factorisation des tests E2E dans un workflow séparé pour une meilleure organisation.
- Ajout de permissions au workflow CI pour une sécurité accrue.
- Mise à jour de l'image Nginx dans le Dockerfile.
- Adaptation des types TypeScript pour les mises à jour de Cunningham, ui-kit, i18next et TypeScript.
- Ajout de support hors ligne pour le contenu via Service Workers, incluant la mise en cache du contenu et des métadonnées.
- Ajout de gestion des erreurs 401 avec redirection vers l'URL actuelle.
- Amélioration de la gestion des erreurs et des exceptions dans le backend.

### Autres changements
- Mise à jour des chaînes de traduction.
- Amélioration du prompt pour la traduction IA legacy.
- Ajout de la possibilité d'utiliser le SDK Mistral pour les fonctionnalités d'IA.
- Corrections de typos dans la documentation (contributing.md).
- Ajout d'une checklist IA au template de Pull Request.
- Ajout d'une politique IA dans la documentation contributing.md.
- Correction de problèmes de compatibilité des instances E2E.
- Suppression de la chaîne de requête `without_content` des clients.
- Ajout d'un favicon par défaut.
- Ajout de tests pour vérifier la compatibilité des instances E2E.
- Amélioration de la configuration Helm pour le niveau de log en debug.
- Correction de bugs mineurs dans l'interface utilisateur et le backend.
- Publication de la version 5.0.0 et 4.8.6.
