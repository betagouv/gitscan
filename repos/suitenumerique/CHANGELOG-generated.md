# Synthèse d'activité : suitenumerique (du 01/05 au 20/09/2026)

## Résumé de l'activité
L'activité récente de la suite est marquée par une montée en puissance significative des outils de collaboration et de communication. L'intégration de la messagerie Matrix dans [hub](/repos/suitenumerique/hub), l'amélioration des capacités vidéo de [meet](/repos/suitenumerique/meet) et l'ajout de fonctionnalités d'intelligence artificielle dans [conversations](/repos/suitenumerique/conversations) offrent des expériences utilisateur de plus en plus riches et interactives.

Parallèlement, l'organisation renforce la souveraineté et la sécurité des données. Cela se traduit par l'introduction de nouveaux mécanismes de chiffrement dans [transfers](/repos/suitenumerique/transfers) et une gestion beaucoup plus granulaire des accès et des permissions dans [drive](/repos/suitenumerique/drive). Ces évolutions garantissent un contrôle accru pour les administrateurs tout en simplifiant l'usage quotidien pour les utilisateurs finaux.

## Sécurité
- **Confidentialité et contrôle des données** : Introduction du chiffrement de bout en bout (E2EE) en option pour [transfers](/repos/suitenumerique/transfers) et mise en place de liens de téléchargement uniques à usage unique dans [st-transfers](/repos/suitenumerique/st-transfers).
- **Protection contre les attaques** : Blocage des requêtes de type SSRF (Server-Side Request Forgery) dans [file-scanner](/repos/suitenumerique/file-scanner) et correction de vulnérabilités critiques (CVE) dans [meet](/repos/suitenumerique/meet).
- **Durcissement des accès et des protocoles** : Implémentation du protocole PKCE pour sécuriser les connexions dans [drive-migrator](/repos/suitenumerique/drive-migrator), renforcement de la sécurité du serveur de mail dans [messages](/repos/suitenumerique/messages) et mise à jour de bibliothèques critiques pour la protection des données dans [people](/repos/suitenumerique/people).
- **Correction de fuites de données** : Résolution d'une potentielle fuite de fichiers temporaires dans [meet-whisperx](/repos/suitenumerique/meet-whisperx).

## Autres changements notables
- **Modernisation de l'architecture et des outils de développement** : Migration de [ui-kit](/repos/suitenumerique/ui-kit) vers une structure monorepo et reconstruction complète du site [docs-website](/repos/suitenumerique/docs-website) avec le framework Astro.
- **Optimisation des performances et de l'expérience utilisateur** : Refonte majeure de l'architecture des permissions dans [drive](/repos/suitenumerique/drive), migration du frontend vers Vite pour [calendars](/repos/suitenumerique/calendars) et optimisation des temps d'inférence pour le traitement vidéo dans [meet-matting](/repos/suitenumerique/meet-matting).
- **Évolutions de l'infrastructure et du déploiement** : Amélioration des capacités de déploiement automatisé via [st-ansible](/repos/suitenumerique/st-ansible) et [st-deploycenter](/repos/suitenumerique/st-deploycenter).

## Dépôts les plus actifs
- [meet](/repos/suitenumerique/meet) : Évolutions majeures de l'interface mobile, de la résolution vidéo (1080p) et de l'accessibilité.
- [docs](/repos/suitenumerique/docs) : Enrichissement des capacités d'édition (mathématiques, diagrammes) et amélioration de l'accessibilité.
- [drive](/repos/suitenumerique/drive) : Mise en place d'un système de restrictions d'accès granulaire et refonte de l'architecture des permissions.
- [hub](/repos/suitenumerique/hub) : Intégration complète de la messagerie Matrix (temps réel, threads, réactions).
- [dictaphone](/repos/suitenumerique/dictaphone) : Optimisation du suivi des transcriptions et de l'expérience mobile (téléchargements en arrière-plan).
- [conversations](/repos/suitenumerique/conversations) : Ajout de nouveaux outils d'IA (génération de présentations) et optimisation de l'interface de chat.
- [ui-kit](/repos/suitenumerique/ui-kit) : Consolidation de la bibliothèque de composants en monorepo et création d'outils de migration.
