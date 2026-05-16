# Synthèse d'activité : mte-dgpr (du 14/04 au 21/04/2026)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de la précision et des fonctionnalités des outils de traitement de textes juridiques. Les développements sur [ocapi](/repos/mte-dgpr/ocapi) visent à faciliter la traçabilité et l'analyse des textes, tandis que [arretify](/repos/mte-dgpr/arretify) progresse vers une nouvelle version majeure avec des améliorations significatives dans la conversion d'arrêtés préfectoraux en HTML, notamment la gestion des tableaux issus de l'OCR et la détection des titres. Ces améliorations devraient faciliter le travail des utilisateurs finaux en leur fournissant des données plus précises et mieux structurées.

## Sécurité
Aucun changement lié à la sécurité n'a été identifié dans les changelogs fournis.

## Autres changements notables
- Refonte du code de statut dans [ocapi](/repos/mte-dgpr/ocapi) avec un ensemble figé de codes d'erreur pour une meilleure gestion des erreurs.
- Intégration du support pour le fournisseur Google/Gemini et des benchmarks LLM dans [ocapi](/repos/mte-dgpr/ocapi).
- Mise à jour de l'exigence de version de Python à 3.12 et déclaration de la dépendance `arretify` dans [ocapi](/repos/mte-dgpr/ocapi).
- Amélioration de la détection de page headers et footers via l'intégration de Mistral OCR 3 dans [arretify](/repos/mte-dgpr/arretify).
- Traitement direct des tableaux en HTML via l'intégration de Mistral OCR 3 dans [arretify](/repos/mte-dgpr/arretify).

## Dépôts les plus actifs
- [ocapi](/repos/mte-dgpr/ocapi) : Amélioration de la détection des abrogations, gestion des annexes et prise en charge de nouveaux formats d'articles.
- [arretify](/repos/mte-dgpr/arretify) : Préparation de la version 0.2.0 avec des améliorations significatives dans la conversion d'arrêtés en HTML, notamment la gestion des tableaux OCR et la détection des titres.
