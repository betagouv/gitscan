# Synthèse d'activité : betagouv (du 22/05 au 22/06)

## Résumé de l'activité
L'activité récente de l'organisation betagouv est marquée par une forte concentration sur l'amélioration de la qualité et de la sécurité des applications existantes, ainsi que par le développement de nouvelles fonctionnalités pour répondre aux besoins des utilisateurs. Plusieurs projets ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités et assurer la compatibilité avec les dernières technologies. Des efforts importants ont également été déployés pour améliorer l'expérience utilisateur, notamment en optimisant les performances, en simplifiant les interfaces et en ajoutant de nouvelles fonctionnalités de recherche et de filtrage. On note également le début de plusieurs nouveaux projets, comme `odice`, qui témoignent de l'engagement continu de betagouv dans l'innovation numérique au service de l'intérêt général. Des projets comme `infomedicament` et `jeveuxaider` ont reçu des mises à jour significatives, améliorant leurs fonctionnalités et leur sécurité.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :
- Correction d'une vulnérabilité XSS potentielle dans [seves](/repos/betagouv/seves).
- Mise à jour de dépendances critiques dans [mes-aides-analytics](/repos/betagouv/mes-aides-analytics) pour corriger des vulnérabilités.
- Correction d'une faille de sécurité dans [mon-entreprise](/repos/betagouv/mon-entreprise).
- Mise à jour de la gem `rack-session` dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) pour corriger une vulnérabilité critique.
- Correction d'une faille de sécurité via la sanitisation du paramètre 'next' dans [jeveuxaider-back](/repos/betagouv/jeveuxaider-back).

## Autres changements notables
- Refonte majeure de l'application [pitchou](/repos/betagouv/pitchou) avec migration vers SvelteKit, Vite et pnpm.
- Passage à la version 2.0 des standards dans [standards](/repos/betagouv/standards).
- Refactorisation de l'API dans [rdv-service-public](/repos/betagouv/rdv-service-public).
- Migration vers Poetry pour la gestion des dépendances dans [infomedicament-dataeng](/repos/betagouv/infomedicament-dataeng).
- Mise à jour de Next.js vers la version 16.2.3 dans [grist-custom-widgets-fr-admin](/repos/betagouv/grist-custom-widgets-fr-admin).
- Refonte du formulaire de création de programme dans [mission-transition-ecologique-back](/repos/betagouv/mission-transition-ecologique-back).

## Dépôts les plus actifs
- [seves](/repos/betagouv/seves) : Amélioration de l'interface utilisateur et correction d'une vulnérabilité XSS.
- [test-sme](/repos/betagouv/test-sme) : Amélioration de l'expérience utilisateur et maintenance technique.
- [sylvasan](/repos/betagouv/sylvasan) : Ajout de l'authentification DSF et amélioration de l'expérience utilisateur.
- [infomedicament](/repos/betagouv/infomedicament) : Amélioration de la recherche et de la présentation des informations sur les médicaments.
- [jeveuxaider-front](/repos/betagouv/jeveuxaider-front) : Refonte des formulaires d'inscription et amélioration du partage de missions.
- [grist-core](/repos/betagouv/grist-core) : Amélioration de l'importation depuis Airtable et correction de bugs.
- [mission-transition-ecologique](/repos/betagouv/mission-transition-ecologique) : Correction de bugs et amélioration de la synchronisation des données.
