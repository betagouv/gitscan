# Synthèse d'activité : suitenumerique (du 29 avril au 21 juillet 2026)

## Résumé de l'activité
La période récente a été marquée par des avancées significatives sur plusieurs fronts. L'organisation a continué à renforcer la sécurité de ses applications, notamment avec des mises à jour de dépendances critiques et l'implémentation de nouvelles mesures de protection (scan antivirus dans [transfers](/repos/suitenumerique/transfers), chiffrement des données dans [accounts](/repos/suitenumerique/accounts)).  Des améliorations majeures ont été apportées à l'expérience utilisateur, avec des refontes d'interfaces (site [docs](/repos/suitenumerique/docs-website), application [calendars](/repos/suitenumerique/calendars)), l'ajout de nouvelles fonctionnalités (liens de téléchargement uniques dans [st-transfers](/repos/suitenumerique/st-transfers), filtres de recherche avancés dans [drive](/repos/suitenumerique/drive)) et une amélioration de la performance (migration vers Vite dans [calendars](/repos/suitenumerique/calendars)). L'intégration de la messagerie Matrix dans [hub](/repos/suitenumerique/hub) constitue une avancée importante vers une communication unifiée.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction de vulnérabilités dans [django-lasuite](/repos/suitenumerique/django-lasuite) et [accounts](/repos/suitenumerique/accounts) via la mise à jour de dépendances.
*   Implémentation d'un scan antivirus pour les fichiers transférés dans [transfers](/repos/suitenumerique/transfers).
*   Renforcement de la sécurité du traitement des données ICS dans [calendars](/repos/suitenumerique/calendars).
*   Protection contre les attaques par décompression et les fichiers PDF volumineux dans [conversations](/repos/suitenumerique/conversations).

## Autres changements notables
*   **Refonte de l'infrastructure :** Migration du frontend de [calendars](/repos/suitenumerique/calendars) vers Vite pour une meilleure performance.
*   **Refonte de l'architecture :** Suppression de Postfix dans [messages](/repos/suitenumerique/messages) au profit d'une implémentation en Python pur.
*   **Intégration :** Intégration de la messagerie Matrix dans [hub](/repos/suitenumerique/hub).
*   **Automatisation :** Ajout d'un chart Helm pour faciliter le déploiement de [gallene-deployment](/repos/suitenumerique/gallene-deployment).
*   **Nouvelles fonctionnalités :** Ajout de l'interface en ligne de commande `st-cli` dans [st-ansible](/repos/suitenumerique/st-ansible) pour la gestion des environnements LST.

## Dépôts les plus actifs
*   [ui-kit](/repos/suitenumerique/ui-kit) : Ajout de nouveaux composants et amélioration de l'accessibilité.
*   [hub](/repos/suitenumerique/hub) : Intégration de la messagerie Matrix et amélioration de l'interface utilisateur.
*   [calendars](/repos/suitenumerique/calendars) : Refonte de la gestion des RSVP et migration vers Vite.
*   [messages](/repos/suitenumerique/messages) : Refonte du MTA-in et amélioration de la sécurité.
*   [docs](/repos/suitenumerique/docs) : Refonte de l'en-tête et amélioration de l'accessibilité.
*   [st-ansible](/repos/suitenumerique/st-ansible) : Ajout d'une interface en ligne de commande pour la gestion des environnements LST.
*   [drive](/repos/suitenumerique/drive) : Ajout de filtres de recherche avancés.
