# Synthèse d'activité : openmaraude (du 05/06 au 12/06)

## Résumé de l'activité
L'activité de la période est principalement concentrée sur le développement des capacités de gestion des suspensions. L'introduction d'une interface visuelle dans [suspension-service](/repos/openmaraude/suspension-service) permet désormais d'afficher l'état de suspension des éléments, offrant ainsi une meilleure visibilité et un nouveau mode d'usage pour les utilisateurs finaux. 

En parallèle, des travaux de préparation ont été menés pour assurer le déploiement et l'accessibilité de l'API de gestion via le web, garantissant ainsi la mise en service prochaine de ces fonctionnalités.

## Autres changements notables
- Configuration de l'infrastructure et du routage DNS pour faciliter l'accès aux services via la gestion de fichiers CNAME dans [suspension-service](/repos/openmaraude/suspension-service) et [suspension-service-api](/repos/openmaraude/suspension-service-api).
- Préparation de l'environnement de déploiement de l'API avec l'ajout d'un point d'entrée web (`index.html`) dans [suspension-service-api](/repos/openmaraude/suspension-service-api).

## Dépôts les plus actifs
- [suspension-service](/repos/openmaraude/suspension-service) : Implémentation de la page de gestion de l'état de suspension.
- [suspension-service-api](/repos/openmaraude/suspension-service-api) : Travaux de configuration technique pour le déploiement de l'API.
