# Synthèse d'activité : demarche-numerique (du 14/08 au 21/08)

## Résumé de l'activité
L'activité de la période est marquée par des avancées significatives en matière d'automatisation et de robustesse des services. L'outil d'extraction de données [la_taupe](/repos/demarche-numerique/la_taupe) franchit un cap technologique avec un nouveau moteur de reconnaissance de texte, permettant un traitement par lots plus précis et rapide des documents bancaires. 

Parallèlement, la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) bénéficie d'une mise à jour majeure de son infrastructure et d'améliorations de l'expérience utilisateur, notamment sur la gestion des comptes. Enfin, [ds_proxy](/repos/demarche-numerique/ds_proxy) gagne en flexibilité pour les infrastructures de stockage, facilitant l'intégration de nouveaux services cloud.

## Sécurité
- Renforcement de la sécurité lors de l'exportation de fichiers ZIP sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Migrations et architecture :** Migration majeure de l'application [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) vers Rails 8.1 et refonte de l'architecture des types de champs.
- **Évolutions technologiques :** Passage à un nouveau moteur OCR (PP-OCR v6) et mise en place d'outils de mesure de performance sur [la_taupe](/repos/demarche-numerique/la_taupe).
- **Infrastructure et stockage :** Extension des capacités de [ds_proxy](/repos/demarche-numerique/ds_proxy) pour supporter les protocoles S3 et Swift, accompagnée d'une simplification des dépendances.
- **Optimisation des performances :** Réduction de la latence de traitement sur [la_taupe](/repos/demarche-numerique/la_taupe) et optimisation des requêtes GraphQL sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Amélioration majeure de la précision de l'extraction de données et ajout du traitement par lots.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Mise à jour structurelle de la plateforme et optimisation des fonctionnalités de gestion de dossiers.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Élargissement des options de stockage et optimisation de la configuration.
