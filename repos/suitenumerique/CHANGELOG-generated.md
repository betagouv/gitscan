# Synthèse d'activité : suitenumerique (du 01/10 au 15/10/2026)

## Résumé de l'activité
La période est marquée par une expansion majeure des capacités de communication, notamment avec l'intégration de la messagerie Matrix dans [hub](/repos/suitenumerique/hub) et une refonte profonde de l'expérience mobile pour [messages](/repos/suitenumerique/messages) et [dictaphone](/repos/suitenumerique/dictaphone). Parallèlement, la gestion des fichiers et du stockage gagne en puissance et en fiabilité grâce aux évolutions de [drive](/repos/suitenumerique/drive) et [transfers](/repos/suitenumerique/transfers).

L'ensemble de l'organisation a fait de la sécurité et de la protection de la vie privée une priorité absolue. Les efforts se sont concentrés sur le durcissement des API, l'intégration de nouveaux outils de détection de malwares et la garantie de la confidentialité des échanges pour les utilisateurs finaux.

## Sécurité
- **Protection contre les attaques et vulnérabilités** : Renforcement des API contre les attaques SSRF ([transfers](/repos/suitenumerique/transfers), [file-scanner](/repos/suitenumerique/file-scanner)) et correction de nombreuses vulnérabilités critiques (CVE) sur les dépendances ([meet](/repos/suitenumerique/meet), [projects](/repos/suitenumerique/projects), [conversations](/repos/suitenumerique/conversations)).
- **Détection de menaces** : Introduction d'un moteur de détection de malwares via le protocole ICAP ([django-lasuite](/repos/suitenumerique/django-lasuite)) et intégration de l'antivirus dans le flux de scan des fichiers ([st-ansible](/repos/suitenumerique/st-ansible)).
- **Confidentialité et vie privée** : Garantie qu'aucune donnée de conversation (prompts) n'est enregistrée dans les journaux ou la télémétrie ([conversations](/repos/suitenumerique/conversations)).
- **Authentification et accès** : Amélioration de la conformité aux standards de sécurité (RFC 9700) et de la gestion des déconnexions ([accounts](/repos/suitenumerique/accounts), [interop](/repos/suitenumerique/interop)), ainsi que le renforcement des permissions sur les domaines ([people](/repos/suitenumerique/people)).
- **Chiffrement** : Adoption de l'algorithme Argon2 pour le hachage des mots de passe ([menshen](/repos/suitenumerique/menshen)).

## Autres changements notables
- **Modernisation des infrastructures de développement** : Lancement d'un dépôt de workflows CI/CD réutilisables pour standardiser les processus de l'organisation ([ci](/repos/suitenumerique/ci)) et migration du frontend de [calendars](/repos/suitenumerique/calendars) vers Vite pour de meilleures performances.
- **Évolutions technologiques majeures** : Reconstruction complète du site de documentation avec Astro ([docs-website](/repos/suitenumerique/docs-website)) et migration du stockage vers RustFS pour [drive](/repos/suitenumerique/drive).
- **Nouveaux services et outils** : Initialisation de nouveaux projets clés comme [encryption](/repos/suitenumerique/encryption) et [gallene-sdk](/repos/suitenumerique/gallene-sdk).

## Dépôts les plus actifs
- [messages](/repos/suitenumerique/messages) : Refonte complète de l'interface mobile et renforcement de la sécurité.
- [drive](/repos/suitenumerique/drive) : Optimisations majeures de performance et nouveaux outils d'administration du stockage.
- [hub](/repos/suitenumerique/hub) : Intégration massive et complète de la messagerie Matrix.
- [meet](/repos/suitenumerique/meet) : Améliorations de l'expérience de partage d'écran, de l'accessibilité et de la sécurité.
- [st-ansible](/repos/suitenumerique/st-ansible) : Extension des services gérés (Conversations, Transfers) et durcissement de l'infrastructure.
