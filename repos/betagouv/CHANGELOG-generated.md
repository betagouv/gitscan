# Synthèse d'activité : betagouv (derniers 7 jours)

## Résumé de l'activité
L'activité de l'organisation betagouv sur les 7 derniers jours a été riche et diversifiée, touchant à la fois l'amélioration de l'expérience utilisateur, la correction de bugs, l'ajout de nouvelles fonctionnalités et le renforcement de la sécurité. Plusieurs projets ont bénéficié de mises à jour significatives, notamment `aides-agri`, `Aidants_Connect`, `mon-entreprise` et `sante-psy`. Des efforts importants ont également été consacrés à la modernisation des infrastructures et des dépendances, ainsi qu'à l'amélioration de la documentation et des tests. L'accent a été mis sur la qualité du code, la sécurité et la satisfaction des utilisateurs.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de la sécurité :

- `sante-psy` : Blocage des adresses IP malveillantes et ajout de `crisp.help` à la Content Security Policy (CSP).
- `zacharie` : Implémentation d'une Content Security Policy (CSP), ajout de headers de sécurité, correction de vulnérabilités et audit des dépendances.

## Autres changements notables
Plusieurs projets ont connu des évolutions techniques majeures :

- `a-just` : Refonte de la configuration de construction (build) du projet et suppression de Babel-cli, esdoc et compodoc pour alléger l'environnement de développement.
- `api-subversions-asso` : Refactoring du code pour renommer les dossiers et fichiers, introduction de "ports to adapters" pour améliorer l'architecture.
- `csplab` : Remplacement de pgvector par Qdrant pour la gestion des vecteurs et suppression d'Elasticsearch.
- `monstagedeseconde` : Migration des tests Cypress vers Playwright pour améliorer la stabilité et la performance.
- `portail-rse` : Remplacement de pipenv par uv pour une meilleure gestion des dépendances.
- `reva` : Suppression de nombreux *feature flags* obsolètes pour simplifier le code.
- `sylvasan` : Refactor de la liste d'enquêtes et partage de code entre le web et le mobile.
- `zacharie` : Refonte du système de routage pour optimiser les performances.

## Dépôts les plus actifs
Voici une liste des dépôts les plus actifs sur la période :

- `a-just` : Amélioration de la stabilité et de la maintenance du projet, corrections de bugs et mises à jour des dépendances.
- `acces-cible` : Amélioration de l'importation et de la gestion des sites web, correction de bugs liés à la lecture des fichiers CSV.
- `aides-agri` : Amélioration de la sécurité, ajout de nouvelles fonctionnalités pour la gestion des aides en back-office.
- `Aidants_Connect` : Ajout de la génération d'attestations, amélioration de la recherche des mandats.
- `mon-entreprise` : Modernisation et maintenance du simulateur, mise à jour des règles de calcul pour 2026.
- `sante-psy` : Amélioration de la sécurité, correction de bugs et amélioration de la recherche dans l'annuaire.
- `reva` : Amélioration de la gestion des enquêtes et de l'application mobile, mises à jour de dépendances.
- `zacharie` : Ajout d'un tableau de bord public, nouvelle interface pour la création de FEI et amélioration de la sécurité.
